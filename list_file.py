#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


class FileInfo:
    def __init__(self, author, title, suffix):
        self.author = author
        self.title = title
        self.suffix = suffix

    def __str__(self):
        return self.author + ' - ' + self.title + self.suffix


def list_file(path):
    files = os.listdir(path)
    file_list = []
    for file in files:
        tp = os.path.splitext(file)
        filename = tp[0]
        suffix = tp[1]
        tp = filename.split(' - ')
        author = tp[0]
        title = tp[1]
        file_info = FileInfo(author, title, suffix)
        print(file_info)
        file_list.append(file_info)
    return file_list


if __name__ == '__main__':
    list_file("/Users/Afauria/PycharmProjects/music/Musics/")
