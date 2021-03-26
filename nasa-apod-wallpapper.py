from api import NasaApi
from pathlib import Path



#set your API key from https://api.nasa.gov/ . Its DEMO_KEY by default
nasaApi = NasaApi()


print(nasaApi.downloadApod(destinationPath=Path().absolute() / 'images' / 'today.jpg' ))