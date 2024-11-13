from rembg import remove
# pip install --user rembg
# https://pypi.org/project/rembg/
from PIL import Image
# pip install pillow
# https://pypi.org/project/pillow/
# https://www.geeksforgeeks.org/python-pillow-a-fork-of-pil/


input_path = 'input/image.png'
output_path = 'output/img-rm2.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
