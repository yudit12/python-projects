""""
JPGtoPNGconverter
 for runing program with arguments
** in pycharm :
- goto  Run
- edit configuration
- set argument in the parameters field  ( for example pokedex\ pngImages\) - two parameters of folders in windows

the porpose : to change format of all images in given folder
from jpg to png  and save the images.png in new folder

"""
print(__doc__)

import sys
import os
from PIL import Image

#grab first and second argument check  if were given
# assumed that directory were given with slash
image_folder= sys.argv[1] #pokedex\
output_folder=sys.argv[2]#  new_folder\
# print(image_folder,output_folder )
# print(os.path .exists(output_folder))

# create new_folder\ if not exists ( folder of png_images)
os.chdir('./images')  # change the path to create new folder  inside of images folder
if not os.path .exists(output_folder):
    os.makedirs(output_folder)

# change each image.jpg to image.png
for filename  in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    clean_name= os.path.splitext(filename)[0] #  file name without .jpg
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}.png','png')