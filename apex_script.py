import requests
import json


def printJson(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def getApiRequest():
    URL = ' https://public-api.tracker.gg/apex/v1/standard/profile/2/Nikezy'
    API_KEY = '8b8c6507-2bf4-4616-8818-dea502e9a86a'
    HEADERS = {'TRN-Api-Key': API_KEY}

    r = requests.get(url=URL, headers=HEADERS)
    data = r.json()

    return data.get('data')


def main():
    data = getApiRequest()

    stats = data.get('stats')

    for item in stats:
        for metadata in item['metadata']:
            print('Data:', metadata)
            if metadata == 'name':
                name = metadata
                print('Name:', name)
        print('\n')


if __name__ == '__main__':
    main()
