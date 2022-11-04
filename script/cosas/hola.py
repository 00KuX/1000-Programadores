from rembg import remove
from PIL import Image

input_path = "perro.jpg"
out_path = "perroo.png"
input = Image.open(input_path)
output = remove(input)
output.save(out_path)