import cv2


image = cv2.imread('kindle.jpg', cv2.IMREAD_GRAYSCALE)
imagem_equalizada = cv2.equalizeHist(image)


novo_tamanho = (1500, 1050)
altura_original, largura_original = image.shape[:2]
largura_novo, altura_novo = novo_tamanho


if largura_original >= largura_novo and altura_original >= altura_novo:
    imagem_redimensionada = cv2.resize(image, novo_tamanho, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
    print("redimencionado")
else:
    imagem_redimensionada = image
    cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
    print("ok")

cv2.waitKey(0)
cv2.destroyAllWindows()