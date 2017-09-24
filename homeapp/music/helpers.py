from os import listdir
from os.path import isfile, join


def getmusic(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
