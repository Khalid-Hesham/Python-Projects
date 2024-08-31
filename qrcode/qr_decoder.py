import re
from pyzbar.pyzbar import decode
from PIL import Image

n = 1
while n != '0':
  path = input("Enter the path of qrcode image: ")
  name = input("Enter image name: ")
  modified_path = re.sub(r"\\", "/", path)
  img_decode = Image.open(f"{modified_path}/{name}.png")
  results = decode(img_decode)
  # print(results)
  for result in results:
        print(result.data.decode('utf-8'))
  n = input("Press 1 to continue\nPress 0 to exit\n")
