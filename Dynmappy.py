import cv2
import os
import sys


class Dynmappy:
    def __init__(self, path="plugins/dynmap/web/tiles/world/flat"):
        self.dynmap_path = path

    def exists(self, file, nexist_path):
        for path in os.listdir(self.dynmap_path):
            if os.path.exists(self.dynmap_path+"/"+path+"/"+file) == True:
                return self.dynmap_path+"/"+path+"/"+file
        if nexist_path == None:
            print('Dynmappy Error: File "' + file +
                  '" is not found', file=sys.stderr)
            sys.exit(1)
        else:
            return nexist_path

    def output(self, hstart, hend, vstart, vend, size=0, output="dynmap.jpg", nexist_path=None):
        cv2.imwrite(output, cv2.vconcat([cv2.hconcat([cv2.imread(self.exists("z" * size + str(i) + "_" + str(
            j) + ".jpg", nexist_path)) for i in range(hstart, hend)]) for j in range(vstart, vend)[::-1]]))
