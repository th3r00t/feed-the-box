import os
import json
from display import Ui
from config import InitialConfig
from config import ReadConfig
from search import TorrentSearch
from config import SearchConfig

global CONFIG
# CONFIG = load_config_file
global Ui
Ui = Ui()
global MAIN_LOOP
MAIN_LOOP = True


def load_config_file():
    path = os.path.abspath(__file__)
    sl = len(__file__)
    path = path[0:-sl]
    try:
        with open(path+'config.json') as f:
            cfg_array = json.load(f)
            config = ReadConfig(cfg_array)
            return config
    except FileNotFoundError:
        global Ui
        InitialConfig(path+'config.json')


SEARCH_CONFIG = SearchConfig()
CONFIG = load_config_file()
session = {
        'conf': CONFIG,
        'sconf': SEARCH_CONFIG
        }

# search = TorrentSearch()
# search.do_search('Ironman')

while MAIN_LOOP:
    Ui.banner()
    Ui.search_box(session)
    search = TorrentSearch()
    results = search.do_search(input())
    search.print_results(results)
#    print('Choose Selection')
#    selection = input()
