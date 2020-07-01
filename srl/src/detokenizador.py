# -*- coding:utf-8-*-
# --------------------------------------------------------------------------- #
#                           Tokenizador Palavras                              #
#                          Marina Coimbra Viviani                             #
#                          rina.coimbra@gmail.com                             #
#                               Orientacao:                                   #
#                           Sandra Maria Aluisio                              #
#                           Magali Sanches Duran                              #
# --------------------------------------------------------------------------- #
#   Este programa detokeniza as sentencas tokenizadas pelo programa Palavras  #
#  ele recebe como argumento uma pasta contendo arquivos que possuam uma ou   #
#  mais sentencas para serem detokenizadas. Ele trabalha com a pontuacao e    #
#  com os hifens.                                                             #
# --------------------------------------------------------------------------- #

import string
import re
import os
import sys
import getopt


# Na epoca que utilizei o programa utilizava essas duas variaveis locais
# PATH_SENTENCE = './sentAnotacaoMaisFrequentes/'
# PATH_RESULTS = './teste/'

# Multiwords acontecem quando ha um palavra=palavra
def remove_multiwords(line):
    n = 1
    while n != 0:
        line, n = re.subn(r"(\S)=(\S)", '\g<1> \g<2>', line)
    return line

# Algumas multiwords acontecem com underscore em vez de =
def remove_multiwords_underscore(line):
    n = 1
    while n != 0:
        line, n = re.subn(r"(\S)_(\S)", '\g<1> \g<2>', line)
    return line

# Troca aspas duplas por simples
def troca_aspas(line):
    return re.sub(r"\"", "'", line)

# Se houver texto envolto por aspas, retira os espacos
def quotes(line):
    return re.sub(r"\s\'\s([^\']*)\s\'\s", " \'\g<1>\' ", line)

# Se hourver texto envolto por estrelas, retira os espacos
def star(line):
    return re.sub(r"\s\*\s(.*)\s\*\s", ' *\g<1>* ', line)

# Retira o espaco a esquerda de certos tipos de pontuacao
def punctuation_left(line):
    return re.sub(r"\s([\.»,;:!?)\]}%]+)", '\g<1>', line)

# Retira o espaco a direita de certos tipos de pontuacao
def punctuation_right(line):
    return re.sub(r"([\[{(#«$]+)\s", '\g<1>', line)

# Remove palavras com o escrito TRAVESSAO pelo proprio travessao
def travessao(line):
    return re.sub(r"\sTRAVESSAO\s", " - ", line)

# Trata o hifen para palavras que possuam -la -las -lo -los
# e que sejam terminadas em r, z ou s
def tratar_hifen(line):
    line = re.sub(r"a[rzs]-\s(l[ao]s?)", "á-\g<1>", line)
    line = re.sub(r"e[rzs]-\s(l[ao]s?)", "ê-\g<1>", line)
    line = re.sub(r"o[rzs]-\s(l[ao]s?)", "ô-\g<1>", line)
    line = re.sub(r"([iu])[rzs]-\s(l[ao]s?)", "\g<1>-\g<2>", line)
    line = re.sub(r"-\sse", "-se", line)
    line = re.sub(r"(\w)-\s(lhes?)", "\g<1>-\g<2>", line)
    line = re.sub(r"(\w)-\s([oa])", "\g<1>-\g<2>", line)
    return line

# Trata a crase em sentencas que apresentam " a a "
def tratar_crase(line):
    line = re.sub(r" a a ", " à ", line)
    line = re.sub(r" a o ", " ao ", line)
    return line

# Escreve as sentencas em um arquivo na pasta de destino
def write_sentences(sentences, filename, PATH_RESULTS):
    fp = open(PATH_RESULTS + filename, 'w')
    j = 0
    for line in sentences:
        fp.write(line)
        j = j + 1
    fp.close

# Pega input e output da linha de comando
def setInputOtput(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return inputfile, outputfile

def detok(sentence):
    sentence = remove_multiwords(sentence)
    sentence = remove_multiwords_underscore(sentence)
    sentence = troca_aspas(sentence)
    sentence = quotes(sentence)
    sentence = star(sentence)
    sentence = punctuation_right(sentence)
    sentence = punctuation_left(sentence)
    sentence = travessao(sentence)
    sentence = tratar_hifen(sentence)
    sentence = tratar_crase(sentence)
    return sentence

def main(filename):
    # Input
    PATH_SENTENCE = ''
    # Output
    PATH_RESULTS = ''

    #PATH_SENTENCE, PATH_RESULTS = setInputOtput(argv)

    #print PATH_SENTENCE
    #print PATH_RESULTS

    fp = open(filename, 'r')
    sentence = []
    for line in fp:
            line = remove_multiwords(line)
            line = remove_multiwords_underscore(line)
            line = troca_aspas(line)
            line = quotes(line)
            line = star(line)
            line = punctuation_right(line)
            line = punctuation_left(line)
            line = travessao(line)
            line = tratar_hifen(line)
            line = tratar_crase(line)
            sentence.append(line)
    write_sentences(sentence, filename, PATH_RESULTS)
    del(sentence)
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1])


