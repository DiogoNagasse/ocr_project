import cv2

image = cv2.imread(r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\redimencionar\kindle.jpg')

if image is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
    exit()
novo_tamanho = (1500, 1050)
largura_novo, altura_novo = novo_tamanho
altura_original, largura_original = image.shape[:2]


if largura_original >= largura_novo and altura_original >= altura_novo:
    imagem_redimensionada = cv2.resize(image, novo_tamanho, interpolation=cv2.INTER_CUBIC)
    print("Imagem redimensionada para", novo_tamanho)
else:
    imagem_redimensionada = image
    print("Imagem mantida no tamanho original")


cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()