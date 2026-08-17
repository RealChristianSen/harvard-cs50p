from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180).filter(ImageFilter.BLUR).filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")
    
main()