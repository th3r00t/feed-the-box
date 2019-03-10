import os
import sys

class Ui:

    def __init__(self):
        h, w = os.popen('stty size', 'r').read().split()
        self.w, self.h = int(w), int(h)
        self.vc = (self.w / 2)
        # https://en.wikipedia.org/wiki/Box-drawing_character#Unicode    
        self.box_h = '\u2501'
        self.box_tl = '\u250F'
        self.box_tr = '\u2513'
        self.box_v = '\u2503'
        self.box_bl = '\u2517'
        self.box_br = '\u251b'
        self.green = '\033[1;32m'
        self.grey_bg = '\033[47m'
        self.clr_term = '\033[m' 
    @staticmethod
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def banner(self):
        sys.stdout.write(self.green)
        title = 'Feed The Box'
        slogan = 'Your media servers hungry, let\'s feed it'
        self.clear()
        print(self.box_tl+self.box_h*(self.w -2)+self.box_tr)
        # sys.stdout.write(self.clr_term)
        print(self.box_v, \
                ' '*(self.center(title)-1), \
                title, \
                ' '*(self.center(title)-2), \
                self.box_v \
                )
        print(self.box_v, \
                ' '*(self.center(slogan)-1), \
                slogan, \
                ' '*(self.center(slogan)-2), \
                self.box_v \
                )
        print(self.box_bl+self.box_h*(self.w -2)+self.box_br)

    def center(self, txt):
        tlen = len(txt)
        center = int((self.vc - (tlen / 2)-1))
        return center
    
    def list(self, items): 
        sys.stdout.write(self.green)
        for item in items:
            try:
                print(self.box_v,
                        items[item]['txt'], 
                        ' '*(self.w - len(items[item]['txt']) - 5 - len(items[item]['value'])),
                        items[item]['value'],
                        self.box_v
                        )
            except TypeError:
                print(self.box_v,
                        items[item]['txt'],
                        ' '*(self.w - len(items[item]['txt']) - 5),
                        self.box_v
                        )
        sys.stdout.write(self.clr_term)
        
    def input(self, options):        
        from pudb import set_trace; set_trace()
        print('Choose an option')
        user_input = input()
        try:
            user_input = int(user_input)
            if user_input < len(options) -1:
                return
            else:
               options[user_input]['value'] = input()
               print(options[user_input][desc], '=', options[user_input]['value'])
        except:
            return
