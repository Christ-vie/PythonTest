import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url,full_name)
download_web_image('https://ionecassius.files.wordpress.com/2019/11/15081910971517.jpg?quality=80&strip=all&w=1024&h=540')