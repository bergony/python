from PIL import Image, ImageFilter

# img = Image.open('./pokedex/pikachu.jpg')
# # filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
# # crooked = filtered_img.rotate(90)
# # resize = filtered_img.resize((300, 300))

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)

# region.save("grey.png", 'png')
# # filtered_img.show()

img = Image.open('./astro.jpg')

# new_img = img.resize((400, 400)) Modo errado de reduzir a image.

img.thumbnail((400, 400))


img.save('thumbnail.jpg')
