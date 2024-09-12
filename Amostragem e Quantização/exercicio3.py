import cv2
import numpy as np
import matplotlib.pyplot as plt

def quantize_image(image, num_levels):
    """
    Quantiza a imagem para um número específico de níveis de intensidade.
    
    Args:
    image (np.array): Imagem original.
    num_levels (int): Número de níveis de intensidade desejados.
    
    Returns:
    np.array: Imagem quantizada.
    """
    # Calcula o fator de quantização
    factor = 256 // num_levels
    
    # Aplica a quantização
    quantized_image = (image // factor) * factor
    
    return quantized_image

# Carregar a imagem
image = cv2.imread('genshas.jpg')

# Converter de BGR para RGB talvez trocar para preto e branco dps
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

quantization_levels = [256, 128, 64, 32, 16, 8, 4, 2]

plt.figure(figsize=(45, 30))
for idx, levels in enumerate(quantization_levels):
    quantized_image = quantize_image(image, levels)
    plt.subplot(2, 4, idx + 1)
    plt.imshow(quantized_image)
    plt.title(f'Quantization Levels: {levels}')
    plt.axis('off')

plt.show()
plt.savefig('quantizacao.png')
