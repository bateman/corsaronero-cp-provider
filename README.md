corsaronero-cp-provider
=======================

A CouchPotatoServer (v2) module to add ilCorsaronero.info as a torrent provider for Italian torrents.

####SETUP INSTRUCTIONS (TLDR)

Download the master branch *https://github.com/bateman/corsaronero-cp-provider/archive/master.zip* and copy the init.py and main.py file
inside "corsaronero" folder into your CouchPotato custom plugin folder (it's under CouchPotato data dir folder).
If you don't know where your CouchPotato data dir folder is, open CouchPotato web interface, then go to: Settings -> About -> Directories

####SETUP INSTRUCTIONS

```
# Download the ilCorsaroNero.info search provider (Italian torrents only, see http://ilcorsaronero.info)
https://github.com/bateman/corsaronero-cp-provider/archive/master.zip

# Shut down CouchPotatoServer, either by opening it up in a browser 
# and going to "Settings" -> "Shutdown", or by terminating the process

# Open your CouchPotatoServer folder and traverse into the torrent providers folder
cd ~/CouchPotatoServer # or wherever you have it stored
cd ./custom_plugins

# Extract the downloaded master.zip into a folder named corsaronero
unzip master.zip -d corsaronero # note, your master.zip might be located somewhere else

# Startup CouchPotatoServer
cd ~/CouchPotatoServer # or wherever you have it stored
python CouchPotato.py

# Now you should see *CorsaNero* as one of the prodivers for Torrents. Note that this 
# providers works only if you put *ita, italian, sub ita* etc. as preferred keywords
# in "Setting" -> "Searcher" -> "Preferred Words". This will give Italian releases
# a higher score.
```

####SHOUT OUT

Thanks to RuudBurger (https://github.com/RuudBurger) for developing CouchPotato, 
and to trymbill (https://github.com/trymbill), for its extra torrent provider, from which I borrowed.
