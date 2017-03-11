from PIL import Image, ImageFont, ImageDraw, ImageColor

def image_add(file_name, text):
	im = Image.open(file_name)
	w, h = im.size
	fnt = ImageFont.truetype('Arial.ttf', size=w//5)
	draw = ImageDraw.Draw(im)
	draw.text((100,100), font=fnt, fill=128, text=text)
	im.show()

image_add('gizen.png', 'gizen')