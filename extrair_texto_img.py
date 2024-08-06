import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

config_personalizada = r'--oem 3 --psm 6'

try:
    imagem = Image.open(r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\imagens_pdfs\kindle.jpg')
except IOError:
    print("Erro ao abrir a imagem. Verifique o caminho e o formato do arquivo.")
    exit()

# Aplique melhorias na imagem
imagem = imagem.convert('L')
imagem = ImageEnhance.Contrast(imagem).enhance(3)
imagem = imagem.filter(ImageFilter.SHARPEN)  
imagem = imagem.filter(ImageFilter.MedianFilter()) 


texto = pytesseract.image_to_string(imagem, lang='por', config=config_personalizada)
print("Texto extraído:")
print(texto)
