import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter location: ')
    print("Retrieving:", url)
    data = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    #zagniezdzone, ./ - zeby nie pisac calej sciezki comments/comment/count
    lst = tree.findall('.//count')
    print("Count:", len(lst))
    sum = 0

    # <name>Chuck</name>
    # <email hide="yes">
    # xml jest jak drzewo, wywolujemy tag: tree.find.name i
    # jego sam element tree.find('name').text - to jest Chuck
    # a hide w email to atrybut nie tekst wiec tree.find('email').get('hide')

    for number in lst:
        sum += int(number.text)
    print('Sum:', sum)

if __name__ == "__main__":
    main()