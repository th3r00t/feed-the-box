import os
import sys

class Ui:

    def __init__(self, **kwargs):
        try:
            h, w = os.popen('stty size', 'r').read().split()
            self.w, self.h = int(w), int(h)
            self.vc = (self.w / 2)
        except: self.w, self.h = 800, 600; self.vc = (self.w / 2)
        # https://en.wikipedia.org/wiki/Box-drawing_character#Unicode
        try:
            if kwargs['path']:
                self.config = kwargs['path']
            elif not self.config:
                self.config = None
        except KeyError:
            pass

        self.box_h = '\u2501'
        self.box_tl = '\u250F'
        self.box_tr = '\u2513'
        self.box_v = '\u2503'
        self.box_bl = '\u2517'
        self.box_blc = '\u2523'
        self.box_br = '\u251b'
        self.box_brc = '\u252b'
        self.green = '\033[1;32m'
        self.grey_bg = '\033[47m'
        self.clr_term = '\033[m' 
    @staticmethod
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner_standalone(self):
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
        print(self.box_blc+self.box_h*(self.w -2)+self.box_brc)

    def line_wrapper(self, line):
        # self.h, self.w
        try:
            justify = line[1]
            line = line[0]
            if justify == 'l':
                print(self.box_v, ' ', line, ' '*(self.w - (len(justify) + 4)), ' ', self.box_v)
            elif justify == 'c':
                print(self.box_v, ' '*(self.center(line)-1), line, ' '*(self.center(line)-2), self.box_v)
            else:
                line_len = len(line)
                ww = self.w - line_len
                print(self.box_v, ' '*ww, line, ' ', self.box_v)
        except KeyError:
                print(self.box_v, ' ', line, ' '*(self.w - (len(justify) + 4)), ' ', self.box_v)

    def search_box(self, session):
        sys.stdout.write(self.green)
        search_prompt = "Choose your search options"
        search_prompt2 = "The default option is to search videos"
        search_prompt3 = "If that is ok then just type your search in below"
        self.line_wrapper([search_prompt, 'c'])
        self.line_wrapper([search_prompt2, 'c'])
        self.line_wrapper([search_prompt3, 'c'])

        """print(
            self.box_v,
            ' '*(self.center(search_prompt)-1),
            search_prompt,
            ' '*(self.center(search_prompt)-2),
            self.box_v
            )
        print(
            self.box_v,
            ' '*(self.center(search_prompt2)-1),
            search_prompt2,
            ' '*(self.center(search_prompt2)-2),
            self.box_v
            )
        print(
            self.box_v,
            ' '*(self.center(search_prompt3)-1),
            search_prompt3,
            ' '*(self.center(search_prompt3)-3),
            self.box_v
            )"""


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
                        ' '*(self.w - len(items[item]['txt']) - 6 - len(items[item]['value'])),
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
        print('Choose an option')
        user_input = input()
        try:
            user_input = int(user_input)
            if user_input > len(options): 
                return
            elif options[user_input]["id"] == "write_config":
               self.write_out(options)
            else:
                self.clear()
                self.banner()
                print('Enter your', options[user_input]['desc'])
                options[user_input]['value'] = input()
                self.clear()
                self.banner()
                self.list(options)
                print(options[user_input]['desc'], '=', options[user_input]['value'])
        except:
            return
