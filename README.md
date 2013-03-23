corsaronero-cp-provider
=======================

A CouchPotatoServer (v2) module to add ilCorsaronero.info as a torrent provider for Italian torrents.

####SETUP INSTRUCTIONS (TLDR)

Download the master branch *https://github.com/bateman/corsaronero-cp-provider/archive/master.zip* and copy it into
your Couch Potato torrent providers folder.

####SETUP INSTRUCTIONS

```
# Download the ilCorsaroNero.info search provider (Italian torrents only, see http://ilcorsaronero.info)
https://github.com/bateman/corsaronero-cp-provider/archive/master.zip

# Download the latest release of BeautifulSoup4 (http://www.crummy.com/software/BeautifulSoup/bs4/download/4.1/)
# The latest is 4.1.2, as of this writing. Due to a bug that prevents from scraping the torrent page, you will 
# have to replace the bs4 subfolder included in CouchPotatoServer 
tar -zxvf beautifulsoup4-4.1.2.tar.gz  # current folder is __WHEREVER__
cd ~/CouchPotatoServer # or wherever you have it stored
cd ./couchpotato/libs
rm -r bs4
mv __WHEREVER__/bs4 .

# Shut down CouchPotatoServer, either by opening it up in a browser 
# and going to "settings" -> "shutdown", or by terminating the process

# Open your CouchPotatoServer folder and traverse into the torrent providers folder
cd ~/CouchPotatoServer # or wherever you have it stored
cd ./couchpotato/core/providers/torrent

# Extract the downloaded master.zip into a folder named deildu
unzip master.zip -d corsaronero # note, your master.zip might be located somewhere else

# Startup CouchPotatoServer
cd ~/CouchPotatoServer # or wherever you have it stored
python CouchPotato.py

# Now you should see *Corsanero* as one of the prodivers for Torrents.
```

####SHOUT OUT

Thanks to RuudBurger (https://github.com/RuudBurger) for developing CouchPotato, 
and to trymbill (https://github.com/trymbill), for its extra torrent provider, from which I borrowed.
