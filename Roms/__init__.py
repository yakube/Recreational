import wikipedia
import re

regex = "(.*\\bnintendo\\b\\s.*)|" \
        "(.*\\bplaystation\\b\\s.*)"
page = wikipedia.page("Home video game console")
consoles = [s for s in page.links if re.match(regex, s, re.IGNORECASE)]
for x in consoles:
    print(x)
