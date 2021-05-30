import Dynmappy


class DynmappyMove:
    def __init__(self, config):
        self.mapnum = 0
        self.config = config
        self.hnow = self.config[self.mapnum]["x"]
        self.vnow = self.config[self.mapnum]["y"]
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def up(self):
        self.vnow += 3
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def down(self):
        self.vnow -= 3
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def right(self):
        self.hnow += 4
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def left(self):
        self.hnow -= 4
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def map(self):
        self.mapnum += 1
        if len(self.config) <= self.mapnum:
            self.mapnum = 0
        self.hnow = self.config[self.mapnum]["x"]
        self.vnow = self.config[self.mapnum]["y"]
        Dynmappy("plugins/dynmap/web/tiles/"+self.config[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")
