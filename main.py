import re
from random import choice, randint

words = re.findall(r"(?<![\d:])\d+(?![\d:])|(?<!\d):(?!\d)|[a-zA-Z_’']+|[.,!?;]", open("10-0.txt", "r").read())
word_grams = list(zip(words, words[1:] + words[:1], words[2:] + words[:2]))
period_grams = [word_grams[x] for x in range(len(word_grams)) if word_grams[x][0] == "."]

f = open("new-book.txt", "w")

chapters = randint(13, 19)
for i in range(chapters):
    verses = randint(23, 29)
    for j in range(verses):
        count = 1
        output = str(i + 1) + ":" + str(j + 1) + " "
        current_grams = period_grams
        c = choice(current_grams)
        while c[-1] != ".":
            current_grams = [word_grams[x] for x in range(len(word_grams)) if
                             word_grams[x][0] == c[1] and word_grams[x][1] == c[2]]
            c = choice(current_grams)
            if len(output) / 60 > count:
                count = count + 1
                output = output + "\n"
            output = output + c[0] + " "
        output = output + c[1] + " "
        output = output + c[2]
        f.write(output + "\n\n")

f.close()
