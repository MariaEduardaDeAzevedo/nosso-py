# coding: utf-8
from PIL import Image
import sys
print """
 >>> E necessario instalar a bibliotela PIL primeiro. <<<
 
  ------------------- Instalacao: -------------------
 LINUX: apt-get install python-imaging
 WINDOWS: http://www.pythonware.com/products/pil/#pil117
  ---------------------------------------------------
  
 >>> A imagem deve estar na mesma pasta que este arquivo
 >>> O arquivo deve ser descrito na entrada com o seu nome
 e seu formato, a exemplo: "img.png"
 >>> A imagem de saida sera salva no mesmo diretorio deste
 arquivo.
"""
img = raw_input('Qual o nome da imagem que voce deseja negativar? ')
image = Image.open(img)
pixels = image.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
		if pixels[i,j] <= (128, 128, 128):
			pixels[i,j] = (255, 255, 255)
		elif pixels[i,j] > (128, 128, 128):
			pixels[i,j] = (0, 0, 0)

image.save("saida.jpg")
print "Veja o resultado em: saida.jpg"
