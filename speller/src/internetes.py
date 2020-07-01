

import re
import cPickle as pickle


if __name__ == '__main__':
	fp = open('net-dic-rexp-pyUTF8.csv','r')
	lines = fp.readlines()
	fp.close()
	
	tokens_list = [line.split(',')[:2] for line in lines]
	rules = [(token[0],token[1]) for token in tokens_list]
	simple_matches = {i:j for i,j in tokens_list if '+' not in i and '*' not in i}
	re_matches = {re.compile(i):j for i,j in tokens_list if '+' in i and '*' in i}

	dict = dict()
	dict['simple'] = simple_matches
	dict['re'] = re_matches
	#if len([j for i,j in rules if (('+' in i or '*' in i) and i.match('muito'))]) > 0:
	#	print [j for i,j in rules if i.match('muito')]
	fp = open('internetes','w')
	pickle.dump(dict,fp)
	fp.close()



