#ocr_extract
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

ocrImageFile = config.get('Local', 'ocr_file')
print (ocrImageFile)


image = cv2.imread(ocrImageFile) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "{}.png".format("temp")
cv2.imwrite(filename, gray)


print(pytesseract.image_to_string(Image.open(filename)))