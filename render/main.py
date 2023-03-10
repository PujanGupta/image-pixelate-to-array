from PIL import Image

def createImg(pixelArray,output):
    width, height = [pixel for pixel in pixelArray.keys()][-1]
    image = Image.new("RGB",(width,height))
    
    for (x, y), hexval in pixelArray.items():
        rgbval = tuple(int(hexval.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        if x < width and y < height:
            image.putpixel((x,y),rgbval)
        
    image.save(output)
