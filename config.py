from display import Ui
import requests

class InitialConfig(Ui):

    def __init__(self, path):
        super().__init__(path=path)
        self.banner()
        a = self.options_array()
        self.list(a)
        initilize = True
        while initilize:
            self.input(a)

    def write_out(self, options):
        import json
        # path = (os.path.abspath(__file__)[0:-len(__file)]+'config.json')
        with open(self.config, 'w') as f:
            json.dump(options, f)
            self.clear()
            self.banner()
            print("Configuration file generated")

    def options_array(self):
        """
        Default values for initial program configuration
        """
        options = {
                0: {
                    "id": "uname",
                    "value": None,
                    "txt": "0: Name",
                    "desc": "Username"
                    },
                1: {
                    "id": "email",
                    "value": None,
                    "txt": "1: Email Address",
                    "desc": "Your Email Address"
                    },
                2: {
                    "id": "msgprefs",
                    "value": False,
                    "txt": "2: Messaging",
                    "desc": "Your Messaging Preferences"
                    },
                3: {
                    "id": "mv_folder",
                    "value": None,
                    "txt": "3: Movie Folder",
                    "desc": "Your Movie Folder"
                    },
                4: {
                    "id": "tv_folder",
                    "value": None,
                    "txt": "4: Tv Folder",
                    "desc": "Your Tv Folder"
                    },
                5: {
                    "id": "write_config",
                    "value": False,
                    "txt": "5: Write Config File",
                    "desc": "Finish Setup"
                    }
            }
        return options


class ReadConfig():
    """
    Returns a usable array of configuration options
    :param cfg_array: raw json array from ./config.json

    .uname
    .email
    .tv_folder
    .mv_folder
    """
    def __init__(self, cfg_array):
        self.uname = cfg_array['0']['value']
        self.email = cfg_array['1']['value']
        self.msgprefs = cfg_array['2']['value']
        self.mv_folder = cfg_array['3']['value']
        self.tv_folder = cfg_array['4']['value']


class SearchConfig():
    def __init__(self):
        self.params()

    def params(self):
        self.array = {
            'all': '0',
            'audio': '100',
            'video': '200',
            'applications': '300',
            'games': '400',
            'porn': '500'
        }
        return self


class TmdApi():
    def __init__(self):
        self.v3key = "a0aaf81ae8e451a7fa098111c4680515"
        self.v4key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMGFhZjgxYWU4ZTQ1MWE3ZmEwOTgxMTFjNDY4MDUxNSIsInN1YiI6IjVjZTE3MGNiYzNhMzY4MjNjNTIxM2JlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._PhSXtQ1mbm_ohLT3SNK-b6noQr5yiTlfYg-K34A7Wo"
        self.docs = "https://developers.themoviedb.org/3/getting-started/introduction"
        self.url = "https://api.themoviedb.org"
        self.headers = {
            'Authorization': 'Bearer {' + self.v4key + '}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
