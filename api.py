import requests
from pathlib import Path
import shutil


class NasaApi():
    def __init__(self, key='DEMO_KEY'):
        self.api_key = key

    def getTodayApodUrl(self):
        return requests.get('https://api.nasa.gov/planetary/apod?api_key=' + self.api_key).json()['url']

    def getTodayApodHdUrl(self):
        return requests.get('https://api.nasa.gov/planetary/apod?api_key=' + self.api_key).json()['hdurl']

    def getRandomApodUrl(self):
        return requests.get('https://api.nasa.gov/planetary/apod?count=1&api_key=' + self.api_key).json()[0]['url']

    def getRandomApodHdUrl(self):
        return requests.get('https://api.nasa.gov/planetary/apod?count=1&api_key=' + self.api_key).json()[0]['hdurl']

    def downloadFile(self, source, destinationPath):
        r = requests.get(source, stream=True)
        if r.status_code == 200:
            with open(destinationPath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            return True
        return False

    def downloadTodaysApod(self, destinationPath=None, hd=True):
        if destinationPath == None:
            destinationPath = Path().absolute() / 'apod.jpg'

        if hd:
            apodUrl = self.getTodayApodHdUrl()
        else:
            apodUrl = self.getTodayApodUrl()

        return self.downloadFile(apodUrl, destinationPath)

    def downloadRandomApod(self, destinationPath=None, hd=True):
        if destinationPath == None:
            destinationPath = Path().absolute() / 'apod.jpg'

        if hd:
            apodUrl = self.getRandomApodHdUrl()
        else:
            apodUrl = self.getRandomApodUrl()

        return self.downloadFile(apodUrl, destinationPath)
