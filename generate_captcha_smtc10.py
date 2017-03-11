from captcha.image import ImageCaptcha
import random, string

raw = ''
im_generator = ImageCaptcha(fonts = ['/Users/Rio/Library/Fonts/ufonts.com_klavika-bold-opentype.otf'])
for i in range(0, 4):
	raw = raw + random.choice(string.letters)
print 'captcha string:', raw
im_generator.write(raw, 'out.png')