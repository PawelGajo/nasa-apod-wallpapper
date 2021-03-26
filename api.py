import requests
from pathlib import Path
import shutil

class NasaApi():
    def __init__(self, key='DEMO_KEY'):
        self.api_key = key

    def getApod(self):
        return requests.get('https://api.nasa.gov/planetary/apod?api_key=' + self.api_key)

    def getApodUrl(self):
        return self.getApod().json()['url']
    
    
    def getApodHdUrl(self):
        return self.getApod().json()['hdurl']

    def downloadApod(self, destinationPath = None):
        if destinationPath == None:
            destinationPath = Path().absolute()

        apodUrl = self.getApodHdUrl()
        r = requests.get(apodUrl, stream=True)
        if r.status_code == 200:
            with open(destinationPath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f) 
            return True
        return False  