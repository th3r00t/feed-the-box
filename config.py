from display import Ui

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
             # TODO Enter main program loop
    
    def options_array(self):
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
