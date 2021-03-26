from nasaapi import NasaApi
from utils import setWallpaper
from pathlib import Path


# destination path with name for downloaded img
imgDestinationPath = Path().absolute() / 'images' / 'apod.jpg'

# #set your API key from https://api.nasa.gov/ . Its DEMO_KEY by default
nasaApi = NasaApi()

# ---- download today's apod and save in destination path. hd parameter defines img resolution.
# nasaApi.downloadTodaysApod(destinationPath=imgDestinationPath)

# ---- download random apod img and save in destination path. hd parameter defines img resolution.
nasaApi.downloadRandomApod(destinationPath=imgDestinationPath)

# set img as wallpaper
setWallpaper(imgDestinationPath)
