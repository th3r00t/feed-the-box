class MagnetDownloader:

    def __init__(self, magnet):
        self.get_magnet(magnet)

    def get_magnet(self, magnet):
        """
        Implement OS call to deluge-console "add magnet" and find a way to specify download directory
        """
        # print(magnet)
        import subprocess
        subprocess.run(["deluge-console","add "+magnet])
