import ctypes

def setWallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path) , 0)