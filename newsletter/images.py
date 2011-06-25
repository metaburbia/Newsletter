import Image
import ImageDraw
import ImageFont

def createCountdown(daysRemaining):
    myfont=ImageFont.truetype('arial.ttf',88)
    text=str(daysRemaining)
    textsize = myfont.getsize(text)
    
    im_x = myfont.getsize(text)[0] + 20
    im_y = myfont.getsize(text)[1] - 4
    
    xpos = im_x / 2  - myfont.getsize(text)[0] / 2
    ypos = im_y / 2  - myfont.getsize(text)[1] / 2
    
    im = Image.new(mode='RGB',size=(im_x,im_y),color=(225,0,0))
    draw  =  ImageDraw.Draw(im)





    draw.text((xpos,ypos),text,fill=(255,255,255),font=myfont)
    
    im.save("countdown.png", "PNG")
