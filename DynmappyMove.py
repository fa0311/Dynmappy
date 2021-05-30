import Dynmappy


class DynmappyMove:
    def __init__(self):
        self.mapnum = 0
        self.maplist = [
            {
                "name": "build_world",
                "x": -5,
                "y": -7
            },
            {
                "name": "resource_world",
                "x": -4,
                "y": -3
            }
        ]
        self.hnow = self.maplist[self.mapnum]["x"]
        self.vnow = self.maplist[self.mapnum]["y"]
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def up(self):
        self.vnow += 3
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def down(self):
        self.vnow -= 3
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def right(self):
        self.hnow += 4
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def left(self):
        self.hnow -= 4
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")

    def map(self):
        self.mapnum += 1
        if len(self.maplist) <= self.mapnum:
            self.mapnum = 0
        self.hnow = self.maplist[self.mapnum]["x"]
        self.vnow = self.maplist[self.mapnum]["y"]
        Dynmappy("../main/plugins/dynmap/web/tiles/"+self.maplist[self.mapnum]["name"]+"/flat").output(
            self.hnow, self.hnow+8, self.vnow, self.vnow+6, 0, "dynmap.jpg", "assets/image/128x128.png")
