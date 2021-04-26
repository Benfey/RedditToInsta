from instabot import Bot
from PIL import Image
import shutil
import os

# https://stackoverflow.com/questions/62293200/upload-images-to-instagram-using-python
# https://www.youtube.com/watch?v=9pZe1VtpFso

def resize(image_pil, width, height):
    '''
    Resize PIL image keeping ratio and using black background.
    '''
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')

def upload_photo(photo, caption):

    try:
        shutil.rmtree("config/")
    except:
        pass

    im = Image.open(photo)
    if (0.8 < (im.width / im.height) < 1.2) == False:
        print("Fixing aspect ratio")
        resize(im, 1000, 1000).save(photo)

    bot = Bot()
    bot.login(username=os.environ['INSTA_ID'], password=os.environ['INSTA_PASSWORD'])
    bot.upload_photo(photo, caption=caption)
