import qrcode, re

n = 1
while n != '0':
  data = input("Enter data or link to encode: ")
  img_encode = qrcode.make(data)
  path = input("Enter path to save the encoded image in: ")
  name = input("Enter image name: ")
  modified_path = re.sub(r"\\", "/", path)
  img_encode.save(f"{modified_path}/{name}.png")
  n = input("Press 1 to continue\nPress 0 to exit\n")