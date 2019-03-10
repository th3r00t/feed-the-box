import os
import json
from display import Ui
from config import InitialConfig
from config import ReadConfig

global CONFIG
# CONFIG = load_config_file
global Ui
Ui = Ui()

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

CONFIG = load_config_file()

