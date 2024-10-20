from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

def format_ascii_string(ascii_str, width):
    ascii_image = ""
    for i in range(0, len(ascii_str), width):
        ascii_image += ascii_str[i:i+width] + "\n"
    return ascii_image

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
        image = resize_image(image, new_width)
        grayscale_img = grayscale_image(image)
        ascii_str = map_pixels_to_ascii(grayscale_img)
        ascii_image = format_ascii_string(ascii_str, grayscale_img.width)
        return ascii_image
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_ascii_to_file(ascii_art, output_file="ascii_art.txt"):
    with open(output_file, "w") as f:
        f.write(ascii_art)

if __name__ == '__main__':
    image_path = input("Enter the path to the image file: ")
    ascii_art = image_to_ascii(image_path)
    
    if ascii_art:
        print(ascii_art)
        save_ascii_to_file(ascii_art, "output_ascii_art.txt")
