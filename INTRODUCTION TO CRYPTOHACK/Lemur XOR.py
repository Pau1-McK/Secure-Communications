from PIL import Image, ImageChops

im1 = Image.open("INTRODUCTION TO CRYPTOHACK\\lemur.png")
im2 = Image.open("INTRODUCTION TO CRYPTOHACK\\flag.png")

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()
im3.save("INTRODUCTION TO CRYPTOHACK/im3.png")