# coding: utf-8
import os
from PIL import Image

# 另一种方式，获取指定后缀的文件名：
# file_exts = ('*.png', '*.jpg', '*.jpeg')
# files = []

# for file_ext in file_exts:
# 	files.extend(glob.glob(file_ext))

def get_list():
	imfile_names = []
	for file in os.listdir('.'):
		if os.path.splitext(file)[1] in ['.jpg', '.png', '.jpeg']:
			imfile_names.append(file)
	return imfile_names

def save_thumbnail(files):
	for file in files:
		im = Image.open(file)
		im2 = resizer(im, 500)
		im2.save(os.path.splitext(file)[0]+'-thumbnail'+os.path.splitext(file)[1])

def resizer(im, square):
	w, h = im.size
	if w >= h:
			h = (float(h) / float(w) * 500)
			w = 500
	else:
		w = (float(w) / float(h) * 500)
		h = 500
	w = int(w)
	h = int(h)
	return im.resize((w, h))

save_thumbnail(get_list())