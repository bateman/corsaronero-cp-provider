from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import simplifyString, tryUrlencode
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.providers.torrent.base import TorrentMagnetProvider
import datetime
import traceback

log = CPLog(__name__)


class CorsaroNero(TorrentMagnetProvider):

	urls = {
		'test': 'http://ilcorsaronero.info',
		'base_url': 'http://ilcorsaronero.info',
		'detail': 'http://ilcorsaronero.info/tor/%d/%s',
		'search': 'http://ilcorsaronero.info/torrent-ita/%d/%s.html',
	}

	### TODO: are animated movies released to DVDrip or Anime category? ###
	cat_ids = [
		(1, 'DVDrip'),
		# (5, 'Anime'),
	]

	http_time_between_calls = 1  # seconds
	cat_backup_id = None

	### TODO: what about movie year and quality? ###
	def _searchOnTitle(self, title, movie, quality, results):
		log.debug("Searching for %s (imdb: %s) (%s) on %s" % (title, movie['library']['identifier'].replace('tt', ''), quality['label'], self.urls['base_url']))

		# Get italian title
		# First, check cache
		cache_key = 'italiantitle.%s' % movie['library']['identifier']
		italiantitle = self.getCache(cache_key)

		if not italiantitle:
			try:
				dataimdb = self.getHTMLData('http://www.imdb.com/title/%s/releaseinfo' % (movie['library']['identifier']))
				html = BeautifulSoup(dataimdb)
				titletable = html.find("table", id='akas')
				for row in titletable.findAll('tr'):
					if row.findAll('td')[0].text == 'Italy' : italiantitle = row.findAll('td')[1].text
			except:
				log.error('Failed parsing iMDB for italian title, using the original one: %s', traceback.format_exc())
				italiantitle = title

			self.setCache(cache_key,italiantitle,timeout = 25920000)
				
		log.debug("Title after searching for the italian one: %s" % italiantitle)

		# remove accents 
		simpletitle = simplifyString(italiantitle)
		data = self.getHTMLData(self.urls['search'] % (1, tryUrlencode(simpletitle)))

		if 'Nessus torrent trovato!!!!' in data:
			log.info("No torrents found for %s on ilCorsaroNero.info.", italiantitle)
			return
		
		if data:
			try:
				html = BeautifulSoup(data)
				resultdiv = html.find('div', attrs={'id': 'left'})
				entries_1 = resultdiv.find_all('tr', attrs={'class':'odd'})
				entries_2 = resultdiv.find_all('tr', attrs={'class':'odd2'})
			
				try:
					self.parseResults(results, entries_1)
					self.parseResults(results, entries_2)
				except:
					log.error('Failed parsing ilCorsaroNero: %s', traceback.format_exc())
						
			except AttributeError:
				log.debug('No search results found.')

	# computes days since the torrent release
	def ageToDays(self, age_str):
		dd_mm_yy = age_str.split('.')
		yyyy = int("20" + dd_mm_yy[2])		
		t1 = datetime.datetime(yyyy, int(dd_mm_yy[1]), int(dd_mm_yy[0]))
		t2 = datetime.datetime.now()
		# actually a datetime.timedelta object
		tdelta = t2 - t1
		# to int
		return tdelta.days

	# retrieves the magnet link from the detail page of the original torrent result
	def getMagnetLink(self, url):
		data = self.getHTMLData(url)
		html = BeautifulSoup(data)
		magnet = html.find('a', attrs={'class': 'forbtn'})['href']
		return magnet
	
	# filters the <td> elements containing the results, if any
	def parseResults(self, results, entries):
		table_order = ['Cat', 'Name', 'Size', 'Azione', 'Data', 'S', 'L']
		
		for result in entries:
			new = {}
			nr = 0
	
			for td in result.find_all('td'):
				column_name = table_order[nr]
				if column_name:
	
					if column_name is 'Cat':
						cat = td.find('a', {'class': 'red'}).text
						# category must be in cat_ids to go on, otherwise break inner cicle and move to next result
						if cat == self.cat_ids[0][1]:  # or cat == self.cat_ids[1][1]:
							log.info("Hit right category: %s is a movie, keep going.", (cat))
							td.next
						else:
							log.info("Wrong category: %s not a movie, skipping.", (cat))
							break										
					elif column_name is 'Name':
						link = td.find('a', {'class': 'tab'})										
						new['name'] = link.text									
					elif column_name is 'Size':
						new['size'] = self.parseSize(td.text)
					elif column_name is 'Azione':
						# retrieve download link
						new['detail_url'] = td.find('form')['action']
						new['id'] = new['detail_url'].split('/')[4]
						# fare richiesta detail url e prendere link magnet
						new['url'] = self.getMagnetLink(new['detail_url'])
					elif column_name is 'Data':
						new['age'] = self.ageToDays(td.find('font').text)
					elif column_name is 'S':
						new['seeders'] = tryInt(td.find('font').text)
					elif column_name is 'L':
						new['leechers'] = tryInt(td.find('font').text)
						### TODO: what about score extras here ??? ###
						new['score'] = 0
	
				nr += 1
	
			if nr == 7:  # only if we parsed all tds (i.e. category was right)
				results.append(new)
				log.debug("New result %s", new)
