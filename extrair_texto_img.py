import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Defina o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configuração personalizada para o Tesseract
config_personalizada = r'--oem 3 --psm 6'

try:
    # Tente abrir a imagem
    imagem = Image.open(r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\imagens_pdfs\kindle.jpg')  # Altere para o caminho correto da imagem
except IOError:
    print("Erro ao abrir a imagem. Verifique o caminho e o formato do arquivo.")
    exit()

# Aplique melhorias na imagem
imagem = imagem.convert('L')  # Converte para escala de cinza
imagem = ImageEnhance.Contrast(imagem).enhance(2)  # Aumenta o contraste
imagem = imagem.filter(ImageFilter.SHARPEN)  # Aplica nitidez

# Extraia o texto especificando o idioma
texto = pytesseract.image_to_string(imagem, lang='por', config=config_personalizada)
print("Texto extraído:")
print(texto)
