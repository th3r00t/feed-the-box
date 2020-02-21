from pathlib import Path
import os

class MagnetDownloader:

    def __init__(self, magnet, dl_type):
        self.get_magnet(magnet, dl_type)

    def get_magnet(self, magnet, dl_type):
        import subprocess as sp
        movie = Path('/srv/ext/Storage/Movies/')
        tv = Path('/srv/ext/Storage/Tv\ Shows/')
        other = Path('/srv/ext/Storage/Torrents/')
        if dl_type == "m":
            location = movie
        elif dl_type == "t":
            location = tv
        elif dl_type == "o":
            location = other
        outfile = sp.DEVNULL
        torrent = "-a %s" % magnet
        location = "-w %s" % location
        cmd = "transmission-remote --download-dir "+location+" -a " + magnet
        os.system(cmd)
