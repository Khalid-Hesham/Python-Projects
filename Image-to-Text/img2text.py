from PIL import Image
import pytesseract, re

def extract_text_from_image(image_path):
    try:
      image = Image.open(image_path)
    except:
       return "Error: Image not found"
    text = pytesseract.image_to_string(image)
    return text

n = 1
while n != '0':
  path = input("Enter your image path: ")
  modified_path = re.sub(r"\\", "/", path)
  name = input("Enter your image name: ")
  txt = extract_text_from_image(f"{modified_path}/{name}")
  print(txt)
  n = input("Press 1 to continue\nPress 0 to exit\n")
