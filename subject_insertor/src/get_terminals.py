from sys import argv
from xml.dom import minidom

with open(argv[1]) as fp:
	dom = minidom.parse(fp)

for s in dom.getElementsByTagName('s'):
	string = ''
	for t in s.getElementsByTagName('t'):
		string += t.attributes['word'].value
		string += ' '
	print string
