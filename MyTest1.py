import urllib.request
import random
def download_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)
download_image('https://....')
