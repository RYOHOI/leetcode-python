import os, re

c_comment, c_empty, c_normal = 0, 0, 0
# iterate over files in one folder
for file in os.listdir('.'):
	if os.path.splitext(file)[1] == '.py':
		# split comment line, empty line and normal line apart
		for line in open(file).readlines():
			if re.search(r'^$', line):
				c_comment += 1
			elif re.search(r'^#', line):
				c_empty += 1
			else:
				c_normal += 1

print "Real code:%r\nComments:%r\nEmpty Lines:%r" % (c_normal, c_comment, c_empty)
