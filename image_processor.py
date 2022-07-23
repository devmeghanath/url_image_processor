from webbrowser import get
import requests
from PIL import Image
from io import BytesIO

url = input("enter the url of image:")


try:
    def get_image_size(url):
        data = requests.get(url).content
        im = Image.open(BytesIO(data))    
        return im.size
    width,height = get_image_size(url)

    print("width of the image is: ",width)
    print("height of the image is: ",height)
    print("size of the image is: ",(width*height)/1000000," MP")
except:
    print("invalid url")

