from PIL import ImageEnhance, Image, ImageFilter
import os

path = './imgs'
pathOut = '/editedimgs'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'./{pathOut}/{clean_name}_edited.jpg')
