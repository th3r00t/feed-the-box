import os
import json
from display import Ui
from config import InitialConfig

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
            CONFIG = json.load(f)
    except FileNotFoundError:
        global Ui
        InitialConfig()

CONFIG = load_config_file()
