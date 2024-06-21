import pytesseract
from PIL import Image

#Definir la ruta de la imagen
ruta_iamgen = 'ejemplo3.jpeg'

#Abrir la imagen con PIL
imagen = Image.open(ruta_iamgen)

#Utilizar pytesseract para obtener el texto de la imagen
texto = pytesseract.image_to_string(imagen)

#Imprimir le texto extraido
print(texto)