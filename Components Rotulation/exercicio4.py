import cv2
import numpy as np
import matplotlib.pyplot as plt

def print_matrix(matrix):
    """
    Print the matrix with proper formatting.
    
    Args:
    matrix (np.array): Matrix to be printed.
    """
    for row in matrix:
        print(' '.join([str(x).rjust(2) for x in row]))
        

def quantize_to_binary(image):
    """
    Quantize the image to binary (black and white).
    
    Args:
    image (np.array): Original image.
    
    Returns:
    np.array: Binary image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    return binary_image

def connected_components_labeling(binary_image):
    """
    Label connected components in the binary image using DFS.
    
    Args:
    binary_image (np.array): Binary image.
    
    Returns:
    np.array: Labeled image with each component assigned a unique label.
    int: Number of connected components.
    """
    height, width = binary_image.shape
    labeled_image = np.zeros((height, width), dtype=np.int32)
    current_label = 0
    
    def dfs(x, y, current_label):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if labeled_image[cy, cx] == 0 and binary_image[cy, cx] == 255:
                labeled_image[cy, cx] = current_label
                # Check 8 neighbors
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        stack.append((nx, ny))

    for y in range(height):
        for x in range(width):
            if binary_image[y, x] == 255 and labeled_image[y, x] == 0:
                current_label += 1
                dfs(x, y, current_label)
    
    return labeled_image, current_label

def display_labeled_image(labeled_image, num_labels):
    """
    Display the labeled image with each component in different colors.
    
    Args:
    labeled_image (np.array): Labeled image.
    num_labels (int): Number of connected components.
    """
    height, width = labeled_image.shape
    output_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Assign random colors to each label
    colors = np.random.randint(0, 255, size=(num_labels + 1, 3), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            if labeled_image[y, x] > 0:
                output_image[y, x] = colors[labeled_image[y, x]]
    
    plt.figure(figsize=(10, 10))
    plt.imshow(output_image)
    plt.title('Labeled Connected Components')
    plt.axis('off')
    plt.show()
    plt.savefig('connected_components.png')

image = cv2.imread('coin.png')

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

binary_image = quantize_to_binary(image)

labeled_image, num_labels = connected_components_labeling(binary_image)

display_labeled_image(labeled_image, num_labels)

# Exibir a matriz rotulada
print("Labeled Image Matrix:")
print_matrix(labeled_image)