import pickle
from os import system

nome = '../rules/es'

fp = open(nome)
arq = pickle.load(fp)
fp.close()

novo_arq = {}
for i,j in arq.items():
	novo_arq[i.decode('utf-8')] = unicode(j.decode('utf-8'))

system('mv '+nome+' '+nome+'.old')

fp = open(nome, 'w')
pickle.dump(novo_arq, fp)
fp.close()
