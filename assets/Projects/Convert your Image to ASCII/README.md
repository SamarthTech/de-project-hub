# 🎞️ Image to ASCII Art 

This Python project allows you to convert any image into ASCII art. It takes an image as input, processes it to grayscale, and maps pixel values to a predefined set of ASCII characters, generating a visual representation of the image using only text characters.

## 🚀 Features
- Converts images to ASCII art using pixel brightness.
- Resizes the image while maintaining the aspect ratio to fit the ASCII character structure.
- Supports output of ASCII art in the console or saving it as a `.txt` file.

## 📚 Tech Stack
- **Python 3**
- **Pillow (PIL)** for image processing

## 💡 How It Works
1. The image is resized to maintain the aspect ratio and fit within the terminal or output space.
2. Each pixel is converted to grayscale, resulting in a brightness value.
3. Brightness values are mapped to a set of ASCII characters based on intensity.
4. The resulting ASCII characters are formatted into an art string and displayed or saved to a file.


## ⚙️ Installation and Setup

Follow these steps to get the bot running locally:

1. Clone the Repository:
```bash
git clone https://github.com/5haiqin/Image-to-ASCII-art.git

```

2. Navigate to the project directory:
```bash
cd Image-to-ASCII-art

```
## 💡 Usage
1. Run the Python script:
```bash
python ascii_art.py
```

4. You will be prompted to enter the path of the image file:
```bash
Enter the path to the image file: img.png
```
3. The ASCII art will be displayed in the terminal and saved in a .txt file (output_ascii_art.txt) in the project directory.


## 🧮 Example Output
Here's what the ASCII output might look like in the terminal:
```bash
@@@@@@@@@@#@@###%%S***++;;:,:,,.                         
@@@@@##%S%%S*+;;;;::::,,,,,,,,,,,,                         
@@##%S*+;;:::,,,,,,,,,,,..,....                           
S*+;;::::,,,,,,....                                        
```

## 🗂️ Project Structure
```bash
|-- ascii_art.py         # Main script to convert image to ASCII
|-- README.md            # Project documentation
|-- requirements.txt     # List of dependencies (Pillow)
```

## 🛠️ Customization
1. Image Size: You can modify the width of the ASCII output by changing the new_width parameter in the script:
```bash
def image_to_ascii(image_path, new_width=100):
```
2.ASCII Characters: You can customize the ASCII character set in the ASCII_CHARS list:
```bash
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
```

## 👨‍💻 Contributing
Feel free to open issues or contribute to the project by submitting a pull request. Please ensure your code is well-documented and includes tests where necessary.

## License
This project is licensed under the MIT License - see the LICENSE file for details.