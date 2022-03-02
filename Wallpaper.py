from PIL import Image, ImageDraw, ImageFont
import textwrap

def get_wallpaper(quote, percent):
    # image_width
    image = Image.open("Ramadan Counter Wallpaper.png")
    font = ImageFont.truetype("ConcertOne-Regular.ttf", 117)
    text1 = quote
    text_color = (113, 40, 0)
    text_start_height = 100
    draw_text_on_image(image, text1, font, text_color, text_start_height)
    image.save('created_image.png')
    # drawArc(400,400, 500, percent, 'created_image.png')

def drawArc(W, H, width, percent, path):
    im = Image.open('created_image.png')
    draw = ImageDraw.Draw(im)
    start = 0

    end = 360*(percent/100)
    draw.pieslice( [ (250,250), (350,350)], start, end, (0,132,164), 50 )
    im.save(path)

def draw_text_on_image(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=25)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.multiline_text( ((image_width - line_width) / 2, y_text), line, font=font, fill=text_color)
        y_text += line_height