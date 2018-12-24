import json
import urllib.request, urllib.parse, urllib.error


def main():
    url = input('Enter location: ')
    uhandle = urllib.request.urlopen(url)
    print('Retrieved', url)
    data = uhandle.read().decode()
    print('Retrieved', len(data), 'characters')

    #json.loads(data) robi all_js - jest to slownik
    try:
        all_js = json.loads(data)
    except:
        all_js = None

    print('Count:', len(all_js['comments']))


    sum = 0
    for js in all_js['comments']:
        sum += int(js['count'])

    print(sum)

if __name__ == "__main__":
    main()