from collections import Counter
import re, glob

# initiate Counter with words in file '0005.py'
# acvwords = re.findall(r'\w+', open('0005.py', 'r').read())

# piece files together
files = ['0000.py', '0004.py']
words = []
for file in files:
	words.extend(re.findall(r'\w+', open(file, 'r').read()))

print Counter(words).most_common(10)
