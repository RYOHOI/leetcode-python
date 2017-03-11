import re

regex = r"\w+"

file = open('sqlbot.txt', 'r').read()
words = re.findall(regex, file)
word_count = len(words)

print words
print '*'*10, '\n', word_count