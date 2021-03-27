# nasa-apod-wallpapper

Script used to download today's or random APOD ([Astronomy Picture of the Day](https://en.wikipedia.org/wiki/Astronomy_Picture_of_the_Day)
)

# How to Use it:

Init NasaApi. It could work with empty api_key parameter (DEMO_KEY will be used), but with limit of 30 requests per IP address per hour and 50 requests per IP address per day.

Get your api_key from https://api.nasa.gov/

```python
from nasaapi import NasaApi

nasaApi = NasaApi(api_key)
```

Function downloadTodaysApod for today's APOD.

```python
downloadTodaysApod(destinationPath)
```

Function downloadRandomApod for today's APOD.

```python
downloadRandomApod(destinationPath)
```

Setting image from path as Wallpaper

```python
from utils import setWallpaper

setWallpaper(imgPath)
```

Setting image as wallpapper works on Win10.
