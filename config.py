from display import Ui

class InitialConfig(Ui):

    def __init__(self):
        super().__init__()
        self.banner()
        a = self.options_array()
        self.list(a)
        initilize = True
        while initilize:
            self.input(a)
    def write_out(self):
        pass 
    
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
                }
            }
        return options

   # def input(self):
   #     from pudb import set_trace; set_trace()
   #     print('Choose an option')
   #     opt = self.options_array()
   #     pntr = input()
   #     pntr = int(pntr)
   #     print('Set ', opt[pntr]['desc'])
#     answer = input()
