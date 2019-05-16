class MagnetDownloader:

    def __init__(self, magnet):
        self.get_magnet(magnet)

    def get_magnet(self, magnet):
        import subprocess as sp
        outfile = sp.DEVNULL
        sp.run(["deluge-console","add "+magnet], stdout=outfile, stderr=outfile)
