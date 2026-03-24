from PIL import Image

# image paths
pikachu_path = "./pikachu.png"
gengar_path = "./gengar.png"

# load images
pikachu = Image.open(pikachu_path).convert("RGBA")
gengar = Image.open(gengar_path).convert("RGBA")

# resize
size = (200, 200)
pikachu = pikachu.resize(size)
gengar = gengar.resize(size)

# blend + overlay
fusion = Image.blend(pikachu, gengar, alpha=0.5)
fusion.show()