import os
import re
from random import randint, choice

words = []
path = "D:\Media\Music\Eminem"
albums = os.listdir(path)
for album in albums:
    songs = os.listdir(path + "\\" + album)
    for song in songs:
        if song.endswith(".lrc"):
            words = words + re.findall(r"(?<![\d:.])\d+(?![\d:])|(?<!\d):(?!\d)|(?<!\d)\.(?!\d)|[a-zA-Z_’']+|[,!?;\n]",
                                       open(path + "\\" + album + "\\" + song, "r").read())
word_grams = list(zip(words, words[1:] + words[:1], words[2:] + words[:2]))
period_grams = [word_grams[x] for x in range(len(word_grams)) if word_grams[x][0] == "\n"]
f = open("new-song.txt", "w")

stanzas = randint(20, 35)
for i in range(stanzas):
    sentences = randint(4, 6)
    for j in range(sentences):
        output = ""
        current_grams = period_grams
        c = choice(current_grams)
        while c[-1] != "\n":
            current_grams = [word_grams[x] for x in range(len(word_grams)) if
                             word_grams[x][0] == c[1] and word_grams[x][1] == c[2]]
            c = choice(current_grams)
            if c[0] != "\n":
                output = output + c[0] + " "
        output = output + c[1] + " "
        output = output + c[2]
        f.write(output)
    f.write("\n")

f.close()