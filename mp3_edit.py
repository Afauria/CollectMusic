#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tinytag import TinyTag
import os

path = "/Users/Afauria/PycharmProjects/music/Musics/"
files = os.listdir(path)
for file in files:
    tp = file[-3:]
    # print(tp)
    if tp != "mp3":
        continue
    filename = file[:-4]
    print(filename)
    # os.rename(file, "tst.mp3")
    tag = TinyTag.get(path+file)
    print(tag.title)
    print(tag.artist)
    print(tag.album)