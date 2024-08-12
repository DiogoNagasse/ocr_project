import cv2

# Carrega a imagem
image = cv2.imread(r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\redimencionar\kindle.jpg')

def redimensionarImagem():
    global image
    if image is None:
        print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
        exit()

    # Define o novo tamanho para a imagem
    novo_tamanho = (1500, 1050)
    largura_novo, altura_novo = novo_tamanho
    altura_original, largura_original = image.shape[:2]

    # Redimensiona a imagem se necessário
    if largura_original >= largura_novo and altura_original >= altura_novo:
        imagem_redimensionada = cv2.resize(image, novo_tamanho, interpolation=cv2.INTER_CUBIC)
        print("Imagem redimensionada para", novo_tamanho)
    else:
        imagem_redimensionada = image
        print("Imagem mantida no tamanho original")

    # Exibe a imagem redimensionada
    cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Salva a imagem redimensionada
    caminho_salvar = r'C:\Users\diogo_nagasse\Desktop\PROJETO_OCR\ocr_project\redimencionar\kindle_redimensionada.jpg'
    cv2.imwrite(caminho_salvar, imagem_redimensionada)
    print(f"Imagem salva em: {caminho_salvar}")

# Chama a função para redimensionar e salvar a imagem
redimensionarImagem()
