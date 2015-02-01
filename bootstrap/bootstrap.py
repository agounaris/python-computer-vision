# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.2.0"


import sys
from .face_detect import FaceDetect
from .rectangle_detect import RectangleDetect


def main():

    if sys.argv[1] == "face":
        face_detect = FaceDetect(sys.argv[2])
        face_detect.execute()
        
    if sys.argv[1] == 'rectangle':
        rectangle_detect = RectangleDetect()
        rectangle_detect.black_rectangle()
