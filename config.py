from display import Ui

class InitialConfig(Ui):

    def __init__(self):
        super().__init__()
        self.banner()
        self.list(self.options_array())

    def write_out(self):
        pass 
    
    def options_array(self):
        options = {
                "name": {
                    "value": None, 
                    "txt": "0: Name"
                    },
                "email": {
                    "value": None,
                    "txt": "1: Email Address"
                    },
                "messaging": {
                    "value": False,
                    "txt": "2: Messaging"
                    },
                "movie_folder": {
                    "value": None,
                    "txt": "3: Movie Folder"
                    },
                "tv_folder": {
                    "value": None,
                    "txt": "4: Tv Folder"
                }
            }
        return options

