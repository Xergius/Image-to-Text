from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# assigning an image from the source path
img = Image.open(r"/home/kali/Downloads/image_test.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
with open('/home/kali/Documents/Web-Projects/text-recognition/text_result.txt', mode ='w') as file:
    file.write(result)
    
print("ready!")
print(result)
