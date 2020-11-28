import requests, json
import urllib.request

cat_url = 'http://aws.random.cat/meow'

def get_new_cat():
    image_url = json.loads(requests.get(cat_url).content)["file"]
    urllib.request.urlretrieve(image_url, "cached_cat_image.png")
    return "cached_cat_image.png"

def check_for_cats(message):
    if(message.content.find("cat") != -1 or message.content.find("cats") != -1 or message.content.find("kot") != -1 or message.content.find("kotek") != -1 or message.content.find("puss") != -1 or message.content.find("meow") != -1):
        get_new_cat()
        return "cached_cat_image.png"
    return ""