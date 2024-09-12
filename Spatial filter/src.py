import numpy as np
import cv2


def aplicar_convolucao(imagem, mascara):
    """
    Aplica a convolução em uma imagem colorida (RGB) com uma dada máscara (filtro).
    """
    # Separar os três canais de cor
    canais = cv2.split(imagem)

    # Aplicar a convolução em cada canal
    canais_filtrados = [cv2.filter2D(canal, -1, mascara) for canal in canais]

    # Combinar os canais de volta em uma imagem colorida
    imagem_filtrada = cv2.merge(canais_filtrados)

    return imagem_filtrada


# Definir máscaras (kernels) para os filtros

# Laplace
mascara_laplace = np.array([[0, 1, 0],
                            [1, -4, 1],
                            [0, 1, 0]])

# Filtro High-Boost (a = 1.5 como exemplo)
a = 1.5
mascara_high_boost = np.array([[-1, -1, -1],
                               [-1, 8 + a, -1],
                               [-1, -1, -1]])

# Separei o roberts para funcionar , a operação dava erro quando fazia nos dois eixos ao mesmo tempo
# Roberts (Horizontal)
mascara_roberts_x = np.array([[1, 0],
                              [0, -1]])

# Roberts (Vertical)
mascara_roberts_y = np.array([[0, 1],
                              [-1, 0]])

# Sobel (Horizontal)
mascara_sobel_x = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])

# Sobel (Vertical)
mascara_sobel_y = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]])

# Prewitt (Horizontal)
mascara_prewitt_x = np.array([[-1, 0, 1],
                              [-1, 0, 1],
                              [-1, 0, 1]])

# Prewitt (Vertical)
mascara_prewitt_y = np.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])

# Carregar imagem
imagem = cv2.imread('eula.jpg')

# Aplicar os filtros
imagem_laplace = aplicar_convolucao(imagem, mascara_laplace)
imagem_high_boost = aplicar_convolucao(imagem, mascara_high_boost)
imagem_roberts_x = aplicar_convolucao(imagem, mascara_roberts_x)
imagem_roberts_y = aplicar_convolucao(imagem, mascara_roberts_y)
imagem_sobel_x = aplicar_convolucao(imagem, mascara_sobel_x)
imagem_sobel_y = aplicar_convolucao(imagem, mascara_sobel_y)
imagem_prewitt_x = aplicar_convolucao(imagem, mascara_prewitt_x)
imagem_prewitt_y = aplicar_convolucao(imagem, mascara_prewitt_y)

# Salvar as imagens resultantes
cv2.imwrite('laplace.jpg', imagem_laplace)
cv2.imwrite('high_boost.jpg', imagem_high_boost)
cv2.imwrite('roberts_x.jpg', imagem_roberts_x)
cv2.imwrite('roberts_y.jpg', imagem_roberts_y)
cv2.imwrite('sobel_x.jpg', imagem_sobel_x)
cv2.imwrite('sobel_y.jpg', imagem_sobel_y)
cv2.imwrite('prewitt_x.jpg', imagem_prewitt_x)
cv2.imwrite('prewitt_y.jpg', imagem_prewitt_y)
