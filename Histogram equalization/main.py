import matplotlib.pyplot as plt
from PIL import Image


def load_image(image_path):
    image = Image.open(image_path).convert("L")
    return image


def compute_histogram(image):
    histogram = [0] * 256
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel_value = image.getpixel((x, y))
            histogram[pixel_value] += 1
    return histogram


def compute_cdf(histogram):
    cdf = [0] * 256
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]
    cdf_min = min([x for x in cdf if x > 0])  # Encontrar o mínimo CDF maior que 0
    cdf_normalized = [(x - cdf_min) * 255 / (cdf[-1] - cdf_min) for x in cdf]
    return cdf, cdf_normalized


def equalize_image(image, cdf_normalized):
    width, height = image.size
    equalized_image = Image.new("L", (width, height))
    for x in range(width):
        for y in range(height):
            pixel_value = image.getpixel((x, y))
            new_pixel_value = int(cdf_normalized[pixel_value])
            equalized_image.putpixel((x, y), new_pixel_value)
    return equalized_image


def plot_histogram(histogram, title):
    plt.figure()
    plt.title(title)
    plt.bar(range(256), histogram, width=1)
    plt.xlim([0, 255])
    plt.show()
    plt.savefig("histogram.png")


def plot_cdf(cdf_normalized):
    plt.figure()
    plt.title('Transformation Function (CDF)')
    plt.plot(cdf_normalized, color='b')
    plt.xlim([0, 255])
    plt.show()
    plt.savefig("cdf.png")


def plot_images(original_image, equalized_image):
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.title('Original Image')
    plt.imshow(original_image, cmap='gray')
    plt.subplot(122)
    plt.title('Equalized Image')
    plt.imshow(equalized_image, cmap='gray')
    plt.show()
    plt.savefig("equalized_image.png")


def main(image_path):
    original_image = load_image(image_path)
    histogram = compute_histogram(original_image)
    cdf, cdf_normalized = compute_cdf(histogram)
    equalized_image = equalize_image(original_image, cdf_normalized)
    equalized_histogram = compute_histogram(equalized_image)

    plot_histogram(histogram, 'Original Histogram')
    plot_cdf(cdf_normalized)
    plot_histogram(equalized_histogram, 'Equalized Histogram')
    plot_images(original_image, equalized_image)


if __name__ == "__main__":
    image_path = "jean.jpeg"  # Substitute with your image path
    main(image_path)
