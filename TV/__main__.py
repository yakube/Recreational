import sys
import wikipedia
import pandas
import re
from numpy import size


def main(argv):
    query = " ".join(argv)
    page = wikipedia.page(wikipedia.search("List of " + query + " Episodes", results=1))
    title = re.sub(r"List of (.*) episodes", "\\1", page.title) + "\n\n"
    formatted = re.sub(r"[^\w-]", "", re.sub(r"\s+", "-", title.lower())[:-1])
    html = page.html().encode("UTF-8")
    tables = pandas.read_html(html)
    season = 1

    html_str = "<div>\n<h1>" + title + "</h1>"

    for table in tables:
        findall = re.findall(r"\d+\s+\d+\s+\d+\s+\".*\"", str(table.to_csv))
        if size(findall) > 0:
            # print("Season " + str(season))
            html_str = html_str + '\n<h2 style="margin-left:5%"><strong>Season ' + str(season) + '</h2>'
            for x in findall:
                link = re.sub(r"\d+\s+\d+\s+(\d+)\s+\"(.*)\"", "https://www11.kisscartoon.love/episode/" + formatted +
                              "-season-" + str(season) + "-episode-\\1/", x)
                episode_name = re.sub(r"\d+\s+\d+\s+(\d+)\s+\"(.*)\"", "\\2", x)
                html_str = html_str + '\n<p style="margin-left:10%"><a href="' + link + '">' + episode_name + '</a></p>'
            season = season + 1
            html_str = html_str + '\n<br>'
    html_str = html_str + "\n</div>"
    html_file = open(formatted + ".html", "w")
    html_file.write(html_str)
    html_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
