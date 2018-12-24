from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # url - sam adres
    # html - caly dokument w bytearray
    # fhand - raczka do dokumentu/strony
    # line - linia z bytearray
    # line.decode() - bytearray zmieniona z utf8 na string unicode
    # urlopen - zjada header, socket nie zjada headera

    # url = input("Enter - "
    # html = urllib.request.urlopen(url).read()

    # fhand = urllib.request.urlopen(url)
    # a nastepnie petla po liniach:
    #for line in fhand
    # line.decode()

    url = input("Enter - ")
    html = urlopen(url, context=ctx).read()
    # nie robimy decode bo czytamy czysty html a nie zawartosc strony
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('span')
    sum = 0
    for tag in tags:
      sum += int(tag.contents[0])
    print(sum)

if __name__ == "__main__":
    main()