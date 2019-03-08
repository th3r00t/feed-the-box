from display import Ui

class InitialConfig(Ui):

    def __init__(self):
        super().__init__()
        self.banner()
        self.list(self.options_array())
        self.input()

    def write_out(self):
        pass 
    
    def options_array(self):
        options = {
                0: {
                    "value": None, 
                    "txt": "0: Name",
                    "desc": "Username"
                    },
                1: {
                    "value": None,
                    "txt": "1: Email Address",
                    "desc": "Your Email Address"
                    },
                2: {
                    "value": False,
                    "txt": "2: Messaging",
                    "desc": "Your Messaging Preferences"
                    },
                3: {
                    "value": None,
                    "txt": "3: Movie Folder",
                    "desc": "Your Movie Folder"
                    },
                4: {
                    "value": None,
                    "txt": "4: Tv Folder",
                    "desc": "Your Tv Folder"
                }
            }
        return options

    def input(self):
        from pudb import set_trace; set_trace()
        print('Choose an option')
        opt = self.options_array()
        pntr = input()
        pntr = int(pntr)
        print('Set ', opt[pntr]['desc'])
        answer = input()
