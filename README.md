# feed-the-box
Python tool to search for and download torrents to your media server, arranging them for consumption (emby, plex, etc...)

# Current Features
The configuration system is completed, and will allow you to set some basic config options. None of these options are implemented yet, but they are being stored in config.json

Aside from this the search system is ~70% complete scraping results from pirate bay and filtering them down to the relevent information... Excepting that s/l count is still missing.

# Future Goals.
* Present search results in the console allowing you to choose to download (n, n n n, n-n) with selectors
* Allow setting media type before downloading, this will facilitate the arangement into requisite folders
* Implement a messaging system to alert on completion &| other events
* ? Cache previous search results (Maybe for quick access to magnet links?) ?