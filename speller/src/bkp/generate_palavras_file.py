def force_encode(string, codec = 'iso-8859-1'):
        try:
            return string.encode(i)
        except:
            return string

def force_decode(string, codecs=['utf8','iso-8859-1']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass

if __name__ == '__main__':
	from sys import argv
	import random
	import os
	
	texto = argv[1].decode('utf-8').encode('iso-8859-1')

	random_file_name = str(random.getrandbits(64))
	os.system("perl callPalavras_flat.pl '"+texto+"' ./"+random_file_name)
	fp = open('./'+random_file_name, 'r')
	output_palavras = fp.read().decode('iso-8859-1').encode('utf-8')
	fp.close()
	#os.system("rm ./"+random_file_name)

	print str(output_palavras)