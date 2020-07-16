
"""
first exercise  on images


"""
from PIL import Image, ImageFilter
# img =Image.open ('./images/pokedex/pikachu.jpg')
# # print(img)# object with all data on the image
# # print(img.format)#jpeg
# # print(img.mode)#RGB
# # print(dir(img))# func, method , attribute of the img
#
# # filtered_img= img.filter(ImageFilter.BLUR)
# # we convert to png  because  png support  this img filters
# # filtered_img.save("blur_pikachu.png",'png')
#
# filtered_img=img.convert('L')# convert to gray scale
# filtered_img.save("gray.png",'png')

"""
https://unsplash.com/
- website to download  for free vary good images  
"""
img =Image.open ('./images/astro.jpg')
print(img.size)
new_img=img.resize((400,400))
new_img.save('thumbnail.jpg') # tiny compere to the original image - but looks squished up
img.thumbnail((400,400))
img.save('thumbnail.jpg')
print(img.size)