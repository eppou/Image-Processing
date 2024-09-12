import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_resolution(image, sample_interval):
    """
    Reduz a resolução espacial da imagem.
    
    Args:
    image (np.array): Imagem original.
    sample_interval (int): Intervalo de amostragem.
    
    Returns:
    np.array: Imagem com resolução reduzida.
    """
    # Pega a altura e a largura da imagem original
    height, width = image.shape[:2]
    
    # Calcula a nova altura e largura
    new_height = height // sample_interval
    new_width = width // sample_interval
    
    # Cria uma nova imagem com a resolução reduzida
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    # Preenche a nova imagem com os valores da imagem original
    for i in range(new_height):
        for j in range(new_width):
            new_image[i, j] = image[i * sample_interval, j * sample_interval]
    
    return new_image

# Carregar a imagem
image = cv2.imread('jean.jpg')

# Converter de BGR para RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Intervalos de amostragem diferentes
sample_intervals = [2, 4, 8, 16,32,64,128, 256]

num_images = len(sample_intervals)
cols = 2
rows = (num_images + cols - 1) // cols

plt.figure(figsize=(45, 30))
for idx, interval in enumerate(sample_intervals):
    reduced_image = reduce_resolution(image, interval)
    plt.subplot(rows, cols, idx + 1)
    plt.imshow(reduced_image)
    plt.title(f'Interval: {interval}')
    plt.axis('on')

# Ajustar o espaçamento entre os subplots
plt.tight_layout(w_pad=3.0, h_pad=1.0)
plt.show()
plt.savefig('amostragem.png')
