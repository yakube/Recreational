# fugit
import os
import sys
import os
from os import listdir
from os.path import isfile, join, isdir
from random import shuffle


def main(argv):
    song_names = []
    if len(argv) <= 0:
        mypath = 'C:\\Users\\cubbe\\Music'
        out_path = 'C:\\Users\\cubbe\\Documents'
    elif len(argv) <= 1:
        mypath = argv[0]
        out_path = 'C:\\Users\\cubbe\\Documents'
    else:
        mypath = argv[0]
        out_path = argv[1]
    top_folders = [f for f in listdir(mypath) if isdir(join(mypath, f)) and f!="Pink Floyd"]
    for top_folder in top_folders:
        mid_path = mypath + "\\" + top_folder
        mid_folders = [f for f in listdir(mid_path) if isdir(join(mid_path, f))]
        for mid_folder in mid_folders:
            file_path = mid_path + "\\" + mid_folder
            only_dirs = [f for f in listdir(file_path) if isdir(join(file_path, f))]
            for directory in only_dirs:
                deep_path = file_path + "\\" + directory
                deep_files = [f for f in listdir(deep_path) if isfile(join(deep_path, f)) and f.endswith(".flac")]
                for x in deep_files:
                    song_names.append(("-play " + x[3:-5] + " " + top_folder).lower())
            only_files = [f for f in listdir(file_path) if isfile(join(file_path, f)) and f.endswith(".flac")]
            for x in only_files:
                song_names.append(("-play " + x[3:-5] + " " + top_folder).lower())
    shuffle(song_names)
    out = open(out_path + "\\Song List.txt", "w", encoding="utf-8")
    for song in song_names:
        out.write(song + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
