ss_words = []
for word in open('sensitive_words.txt').readlines():
	ss_words.append(word.strip('\n'))

while True:
	print "input 'exit' to quit\n"
	in_word = raw_input('> ')
	if in_word == 'exit':
		break
	elif in_word in ss_words:
		print 'Caution!!!'
	else:
		print 'Safe & Sound'


