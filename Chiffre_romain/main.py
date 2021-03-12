from PIL import Image,ImageFont,ImageDraw
from random import randint
img=Image.new('RGBA',(900,900),'black')
s="Now"
st=s*25
font=ImageFont.truetype("arial.ttf",20)
w, h= font.getsize(st)
draw=ImageDraw.Draw(img)
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
draw.text((0,0),st, font=font, fill=(r,g,b))

img.show()
img.save("c:\\Users\\Diatemba\\Desktop\\one.png")


height=h

while height<900:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    lt=randint(0,len(s)-1)
    draw.text((0,height),s[lt:len(s)]+st, font=font, fill=(r,g,b))
    height=height+h
img.show()
img.save("c:\\Users\\Diatemba\\Desktop\\two.png")


img1=Image.new('RGBA',(900,900),'black')
# font1=ImageFont.truetype("C:\Python projects\\fnt.ttf",300)
w, h= font1.getsize("Code It")
draw1=ImageDraw.Draw(img1)
draw1.text(((900-w)/2,(900-h)/2),"Code It", font=font1, fill='white')
img1.save("c:\\Users\\Diatemba\\Desktop\\three.png")
img1.show()


for i in range(900):
    for j in range(900):
        k=img1.getpixel((i,j))
        if k==(255,255,255,255):
            img1.putpixel((i,j),img.getpixel((i,j)))
img1.show()
img1.save("c:\\Users\\Diatemba\\Desktop\\four.png")