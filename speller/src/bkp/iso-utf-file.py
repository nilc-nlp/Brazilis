from sys import argv
with open(argv[1]) as fp:
	content = fp.read()
fp = open(argv[1]+argv[2], 'w')
fp.write(content.decode('iso8859').encode('utf-8'))
fp.close()
