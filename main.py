from PIL import Image, ImageDraw, ImageFont
import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

charArray =list(chars)
charlength = len(charArray)
interval = charlength/256
ScaleFactor = 0.3
onecharwidth =8
onecharheight = 18

def getChar(inpuInt):
    return  charArray[math.floor(inpuInt*interval)]

text_file = open("output.txt","w")
font = ImageFont.truetype('C:\\Windows\\Fonts\\Tahoma.ttf',15)
im = Image.open("image.jpg")
width, height = im.size
im = im.resize((int(ScaleFactor*width), int(ScaleFactor*height*(onecharwidth/onecharheight))), Image.NEAREST)
width, height = im.size
pix = im.load()
outputImage = Image.new('RGB', (onecharwidth *width, onecharheight*height), color = (0,0,0))
d=ImageDraw.Draw(outputImage)
print(width, height)

for i in range(height):
    for j in range(width):
        r,g,b=pix[j,i]
        h=int(r/3+g/3+b/3)
        pix[j,i] = (h,h,h)
        text_file.write(getChar(h))
        d.text((j*onecharwidth, i*onecharheight),getChar(h), font = font, fill = (r,g,b))
    text_file.write('\n')

outputImage.save('ascii.jpg')
