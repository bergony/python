import sys
import os
from PIL import Image

import glob


# Pegar primeiro e segundo argumento
pathImage = sys.argv[1]
pathNewImage = sys.argv[2]


# Verificar se exite a pasta se nao criar
if not os.path.isdir(pathImage+pathNewImage):
    os.mkdir(pathImage+pathNewImage)


# Interar pela pokedex
path = pathImage+'*.jpg'

images = glob.glob(path)


for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        nome = file.name[8:-3]
        print(pathImage+pathNewImage+nome+'png')
        img.save(pathImage+pathNewImage+nome+'png')
