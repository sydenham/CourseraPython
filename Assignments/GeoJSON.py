import json
import ssl
import urllib.request, urllib.parse, urllib.error


def main():
    #API url z dokumentacji, do ktorego dodajemy szukany adres -
    # to jest do srony Chucka na potrzeby zadania
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    address = input('Enter location: ')

    #dodajemy szukane miejsce do url - urllib przerabia je na czytelne dla API
    parms = dict()
    parms['address'] = address
    api_key = 42
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #print(json.dumps(js, indent=2))

    place = js['results'][0]['place_id']
    print(place)

if __name__ == "__main__":
    main()