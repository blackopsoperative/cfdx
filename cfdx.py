import urllib.request
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from format import out

URL = input("Put in CFake link: ")

req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')

def download(urls):
    image = urls[0]
    image = image[0]
    dir_name = "CFDX"
    try:
        os.mkdir(dir_name)
    except:
           pass

    for img in urls:
       image = str(img)
       out.info(f"Downloaded: {image}")
       name = fn
       req = urllib.request.Request(image, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
       with urllib.request.urlopen(req) as f:
            imageContent = f.read()
            with open(f"{dir_name}/{name}", "wb") as f:
                 f.write(imageContent)

for img in soup.findAll(id='img_media'):
    imglist = []
    src = img.get('src')
    global yearsplit, fn
    photourl = "https://cfake.com/medias/photos/"
    yearsplit = src.split("/")[3]
    fn = src.split("/")[4]
    imglist.append(f"{photourl}{yearsplit}/{fn}")
    download(imglist)
