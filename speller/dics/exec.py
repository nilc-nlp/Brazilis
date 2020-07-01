import pickle

def AB_IN_UM(filename):
	'''
	AB, IN, UM
	'''
	with open(filename) as fp:
		lines = [line.split(';') for line in fp.readlines()]
	dic = {}
	for line in lines:
		dic[line[0].strip().decode('utf-8')] = line[1].strip().decode('utf-8')
	with open(filename.lower()[:2], 'w') as fp:
		pickle.dump(dic, fp)
	

def NP(filename):
	'''
	NP
	'''
	with open(filename) as fp:
		lines = [line.split(';') for line in fp.readlines()]
	dic = {}
	for line in lines:
		if line[1] != '\r\n':
			dic[line[0].lower().strip().decode('utf-8')] = line[1].capitalize().strip().decode('utf-8')
		else:

			dic[line[0].lower().strip().decode('utf-8')] = line[0].strip().decode('utf-8')
	with open(filename.lower()[:2], 'w') as fp:
		pickle.dump(dic, fp)
	

def ES(filename):
	'''
	ES
	'''
	with open(filename) as fp:
		lines = [line.split(';') for line in fp.readlines()]
	dic = {}
	for line in lines:
		if line[1] != '\r\n':
			dic[line[0].lower().strip().decode('utf-8')] = line[1].capitalize().strip().decode('utf-8')
		else:

			dic[line[0].lower().strip().decode('utf-8')] = line[0].capitalize().strip().decode('utf-8')
	with open(filename.lower()[:2], 'w') as fp:
		pickle.dump(dic, fp)
	

def SI(filename):
	'''
	SI
	'''
	with open(filename) as fp:
		lines = [line.split(';') for line in fp.readlines()]
	dic = {}
	for line in lines:
			dic[line[0].lower().strip().decode('utf-8')] = line[0].upper().strip().decode('utf-8')
	with open(filename.lower()[:2], 'w') as fp:
		pickle.dump(dic, fp)
	

if __name__ == '__main__':
	AB_IN_UM('AB_dict')
	AB_IN_UM('IN_dict')
	AB_IN_UM('UM_dict')
	NP('NP_dict')
	ES('ES_dict')
	SI('SI_dict')
