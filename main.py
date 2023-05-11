import pytesseract
from PIL import Image

def copy_text_from_image(url, language):
    img = Image.open(url)
    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

    file_name = img.filename
    file_name = file_name.split('.')[0]

    custom_config = r'--oem 3 --psm 6'

    text = pytesseract.image_to_string(img, lang=language, config=custom_config)
    print(text)

    with open(f'{file_name}.txt', 'w', encoding='utf8') as text_file:
        text_file.write(text)

url = input('Link to photo: ') # file/...
lang = input('Language to photo: ') # rus, eng, jpn

copy_text_from_image(url, lang)


# -psm N  Set Tesseract to only run a subset of layout analysis and 
# assume a certain form of image. The options for N are:
#     0 = Orientation and script detection (OSD) only.
#     1 = Automatic page segmentation with OSD.
#     2 = Automatic page segmentation, but no OSD, or OCR.
#     3 = Fully automatic page segmentation, but no OSD. (Default)
#     4 = Assume a single column of text of variable sizes.
#     5 = Assume a single uniform block of vertically aligned text.
#     6 = Assume a single uniform block of text.
#     7 = Treat the image as a single text line.
#     8 = Treat the image as a single word.
#     9 = Treat the image as a single word in a circle.
#     10 = Treat the image as a single character.
