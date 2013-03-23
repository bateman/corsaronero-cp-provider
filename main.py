from bs4 import BeautifulSoup
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.providers.torrent.base import TorrentMagnetProvider
import re
import traceback

log = CPLog(__name__)


class CorsaroNero(TorrentMagnetProvider):

	urls = {
		'test': 'http://ilcorsaronero.info/',
		'base_url': 'http://ilcorsaronero.info/',
		'detail': 'http://ilcorsaronero.info/tor/%d/%s',
		'search': 'http://ilcorsaronero.info/argh.php?search=%s %s',
	}

	cat_ids = [
		([1], ['DVDrip']),
		([5], ['Anime']),
	]

	http_time_between_calls = 1 #seconds
	cat_backup_id = None

	def _searchOnTitle(self, title, movie, quality, results):
		data = self.getHTMLData(self.urls['search'] % (title, quality))
		#data = self.getHTMLData(self.urls['search'] % ('m', movie['library']['identifier'].replace('tt', '')))

		if data:
			#cat_ids = self.getCatId(quality['identifier'])
			table_order = ['&nbsp;Name<br>', 'Size<br>', 'Azione<br>', 'Data&nbsp;&#8595<br>', 'S<br>', 'L<br>']

			try:
				html = BeautifulSoup(data)
				resultdiv = html.find('tr', attrs = {'class':'odd'})
				for result in resultdiv.find_all('td', recursive = True):
					print result.get('id').lower()
					## td class lista
					if result.get('id').lower() not in cat_ids:
						continue

					try:
						for temp in result.find_all('tr'):
							if temp['class'] is 'firstr' or not temp.get('id'):
								continue

							new = {}

							nr = 0
							for td in temp.find_all('td'):
								column_name = table_order[nr]
								if column_name:

									if column_name is 'name':
										link = td.find('div', {'class': 'torrentname'}).find_all('a')[1]
										new['id'] = temp.get('id')[-8:]
										new['name'] = link.text
										new['url'] = td.find('a', 'imagnet')['href']
										new['detail_url'] = self.urls['detail'] % link['href'][1:]
										new['score'] = 20 if td.find('a', 'iverif') else 0
									elif column_name is 'size':
										new['size'] = self.parseSize(td.text)
									elif column_name is 'age':
										new['age'] = self.ageToDays(td.text)
									elif column_name is 'seeds':
										new['seeders'] = tryInt(td.text)
									elif column_name is 'leechers':
										new['leechers'] = tryInt(td.text)

								nr += 1

							results.append(new)
					except:
						log.error('Failed parsing KickAssTorrents: %s', traceback.format_exc())

			except AttributeError:
				log.debug('No search results found.')

	def ageToDays(self, age_str):
		age = 0
		age_str = age_str.replace('&nbsp;', ' ')

		regex = '(\d*.?\d+).(sec|hour|day|week|month|year)+'
		matches = re.findall(regex, age_str)
		for match in matches:
			nr, size = match
			mult = 1
			if size == 'week':
				mult = 7
			elif size == 'month':
				mult = 30.5
			elif size == 'year':
				mult = 365

			age += tryInt(nr) * mult

		return tryInt(age)
