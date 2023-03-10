from PIL import Image

def pixelateToArray(pngImage):
    image = Image.open(pngImage)
    image = image.convert("RGB")
    width, height = image.size
    
    pixels = {}
    
    for y in range(height):
        for x in range(width):
            r,g,b=image.getpixel((x,y))
            hexval = "#{:02x}{:02x}{:02x}".format(r,g,b)
            pixels.update({
                (x,y):hexval
            })
    
    return pixels
