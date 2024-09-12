import cv2
import numpy as np
import matplotlib.pyplot as plt


# Função para ler e preparar imagens
def prepare_image(image_path, target_size):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return None

    # Converter para RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Normalizar se necessário
    if image.max() > 255:
        image = (image / image.max()) * 255

    # Redimensionar para o tamanho desejado
    image = cv2.resize(image, target_size)

    return image


# Função para realizar operações aritméticas
def apply_operations(image, constant):
    added = cv2.add(image, constant)
    subtracted = cv2.subtract(image, constant)
    multiplied = cv2.multiply(image, constant)
    divided = cv2.divide(image, constant)

    return added, subtracted, multiplied, divided


# Função para combinar duas imagens
def combine_images(image1, image2, alpha, beta, gamma):
    return cv2.addWeighted(image1, alpha, image2, beta, gamma)


# Caminhos para as imagens
image_path1 = 'pal.jpg'
image_path2 = 'pok.jpg'

# Tamanho desejado para as imagens
target_size = (500, 500)

# Ler e preparar as imagens
image1 = prepare_image(image_path1, target_size)
image2 = prepare_image(image_path2, target_size)

if image1 is None or image2 is None:
    print("Erro ao carregar as imagens. Verifique os caminhos e tente novamente.")
    exit()

# Aplicar operações aritméticas
constant = 50
added, subtracted, multiplied, divided = apply_operations(image1, constant)

# Combinar imagens
alpha, beta, gamma = 0.5, 0.5, 0
combined_image = combine_images(image1, image2, alpha, beta, gamma)

# Mostrar as imagens
fig, axs = plt.subplots(2, 4, figsize=(20, 10))

axs[0, 0].imshow(image1)
axs[0, 0].set_title("Imagem Original 1")
axs[0, 1].imshow(added)
axs[0, 1].set_title(f"Imagem + {constant}")
axs[0, 2].imshow(subtracted)
axs[0, 2].set_title(f"Imagem - {constant}")
axs[0, 3].imshow(multiplied)
axs[0, 3].set_title(f"Imagem * {constant}")

axs[1, 0].imshow(image2)
axs[1, 0].set_title("Imagem Original 2")
axs[1, 1].imshow(divided)
axs[1, 1].set_title(f"Imagem / {constant}")
axs[1, 2].imshow(combined_image)
axs[1, 2].set_title("Imagem Combinada")
axs[1, 3].axis('off')

for ax in axs.flat:
    ax.axis('off')

plt.show()
plt.savefig('resultado.png')


# Análise dos resultados
def analyze_results(image1, added, subtracted, multiplied, divided, combined_image):
    print("Comparação da Imagem Original com as Resultantes:")
    print("Imagem Original vs Imagem + Constante:")
    print("- Contraste aumentado, brilho geral aumentado.")

    print("Imagem Original vs Imagem - Constante:")
    print("- Contraste diminuído, brilho geral diminuído.")

    print("Imagem Original vs Imagem * Constante:")
    print("- Contraste e brilho ajustados de acordo com o valor da constante.")

    print("Imagem Original vs Imagem / Constante:")
    print("- Contraste e brilho ajustados inversamente ao valor da constante.")

    print("Imagem Original vs Imagem Combinada:")
    print("- Influência das duas imagens controlada pelos pesos alpha e beta.")

    # Você pode adicionar mais detalhes de análise conforme necessário


analyze_results(image1, added, subtracted, multiplied, divided, combined_image)
