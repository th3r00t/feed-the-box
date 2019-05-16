class MagnetDownloader:

    def __init__(self, magnet, dl_type):
        self.get_magnet(magnet, dl_type)

    def get_magnet(self, magnet, dl_type):
        import subprocess as sp
        movie = "/srv/ext/Storage/Movies/"
        tv = "/srv/ext/Storage/Tv Shows/"
        other = "/srv/ext/Storage/Torrents/"
        if dl_type == "m":
            location = movie
        elif dl_type == "t":
            location = tv
        elif dl_type == "o":
            location = other
        outfile = sp.DEVNULL
        # sp.run(["deluge-console","--path=/srv/ext/Storage/"+location+" add "+magnet], stdout=outfile, stderr=outfile)
        sp.run(["deluge-console","--path=/srv/ext/Storage/"+location+" add "+magnet])
