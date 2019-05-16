class MagnetDownloader:

    def __init__(self, magnet, dl_type):
        self.get_magnet(magnet, dl_type)

    def get_magnet(self, magnet, dl_type):
        import subprocess as sp
        movie = "/srv/ext/Storage/Movies/"
        tv = "/srv/ext/Storage/Tv Shows/"
        other = "/srv/ext/Storage/Torrents/"
        if dl_type == "movie":
            location = movie
        elif dl_type == "tv":
            location = tv
        elif dl_type == "other":
            location = other
        outfile = sp.DEVNULL
        sp.run(["deluge-console -p" + location,"add "+magnet], stdout=outfile, stderr=outfile)