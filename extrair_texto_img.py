import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#resolver b.o com caracteres unicos como "ç"
custom_config = r'--oem 3 --psm 6'

try:
    image = Image.open('a')
except IOError:
    print("Erro ao abrir a imagem. Verifique o caminho e o formato do arquivo.")
    exit()

# Aplique melhorias na imagem
image = image.convert('L')  
image = ImageEnhance.Contrast(image).enhance(2) 
image = image.filter(ImageFilter.SHARPEN)  



text = pytesseract.image_to_string(image, lang='por', config=custom_config)
print("Texto extraído:")
print(text)
