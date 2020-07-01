# -*- coding: utf-8 -*-

'''
@Developed by: Nathan Siegle Hartmann
05-12-2014 (english format)
v 1.2
'''

from nltk.tokenize import RegexpTokenizer
from sys import argv
from os import system, listdir
import string
import re
import enchant 
import codecs
import cPickle as pickle
import MySQLdb as mdb
from multiprocessing import Pool
import sqlite3
RULES_PATH = '../rules/'

vowel_pattern = re.compile(r'(a|e|i|o|u)\1{2,}')
special_pattern = re.compile(r'(['+re.escape(string.punctuation)+r'])\1+')
consonant_pattern = re.compile(r'(q|w|t|y|p|d|f|g|h|j|k|l|ç|z|x|c|v|b|n|m)\1{1,}|(r|s)\2{2,}')
laugh_pattern = re.compile(r'(rs|ha|hu|hua|ahu|hau|kk|he){2,}')

spell_dict = enchant.Dict('pt_BR')

rules = dict((file, pickle.load(open(RULES_PATH+file,'r'))) for file in listdir(RULES_PATH))


connection = sqlite3.connect('delaf.database')
cursor = connection.cursor()

def in_delaf(word):
	# connection = mdb.connect('localhost', 'brazilis', 'nilc@clin', 'delaf')	
	# cursor = connection.cursor()
	cursor.execute('select * from delaf where word = "'+ word+'"')
	if len(cursor.fetchall()) > 0:
		return True
	else:
		return False
	#if len(cursor.fetchall()) > 0:
	#	connection.close()
	#	return True
	#else:
	#	connection.close()
	#	return False
	

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def force_decode(string, codecs=['utf-8','iso-8859-1']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
        	pass
    return string


def correct_word(arguments):
	'''
	Use the rules set to correct a wrong word

	@input: word: a word 
		rules: dict() of rules
	@output: a word corrected
	'''
	word = arguments[0]
	user_rules = arguments[1]	
	word = force_decode(word)
	for rule in user_rules:
		if rule == 'in':
			vowel_repeats = [match.group() for match in vowel_pattern.finditer(word)]
			consonant_repeats = [match.group() for match in consonant_pattern.finditer(word)]
			special_repeats = [match.group() for match in special_pattern.finditer(word)]
			laughs = [match.group() for match in laugh_pattern.finditer(word)]
			for i in vowel_repeats:
				word = word.replace(i, i[0])
			for i in consonant_repeats:
				if i[0] in ['r', 's']:
					word = word.replace(i, i[:2])
				else:
					word = word.replace(i, i[0])
			for i in special_repeats:
				word = word.replace(i, i[0])
			for i in laughs:
				word = word.replace(i, '')
		elif rule == 'as':
			#word_lower = word.lower() if len(user_rules) == 7 else word
			word_lower = word.lower()
			if word_lower not in ['.',',',':',';','"',"'",'[',']','+','-','_','(',')','?','!', '/', '\\' ] and not is_number(word) and not in_delaf(word_lower):
				try:
					return spell_dict.suggest(word_lower)[0]
				except:
					return word
			else:
				return word

		if word in rules[rule].keys():
			return rules[rule][word]
	return word


def correct_sentence(sentence, user_rules):
	if len(sentence) >= 8:
		pool = Pool(processes=8)
		results = pool.map(correct_word, [[i,user_rules] for i in sentence])
	else:
		results = [correct_word([word, user_rules]) for word in sentence]
	return results


def read_tmp_file(filename):
	with open(filename) as fp:
		user_rules = fp.readline().strip().split()
		sentence = fp.read()
	return sentence, user_rules


if __name__ == '__main__':
	
	#try:
		sentence, user_rules = read_tmp_file(argv[1])
		sentence = [force_decode(i).lower() for i in sentence.split()] if len(user_rules) == 7 else [force_decode(i) for i in sentence.split()]
		results = correct_sentence(sentence, user_rules)
		print ' '.join(results).encode('utf-8')

		
	#except:
	#	print "Error! Please, contact support."
                connection.close()
