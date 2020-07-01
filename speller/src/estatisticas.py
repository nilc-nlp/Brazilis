#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter
import io

LABELS = ['ac', 'ok', 'co', 'ner', 'si', 'it', 'in', 'es', 'fr', 'dd', 'parte','ital']


def filter_file(input, output):

    file = open(input, 'r')
    lines = file.readlines()
    file.close()

    tokens_list = [line.split()[1:] for line in lines if int(line.split()[0]) not in [7,6,5,4,2,1]]

    file = open(output, 'w')

    for tokens in tokens_list:
        if len(tokens) > 2:
            if tokens[-1:][0].strip() in LABELS or tokens[-2:-1][0].strip() in LABELS:
                for token in tokens:
                    file.write(token.lower() + '\t')
                file.write('\n')

    file.close()

def cria_grupos(input, intervals):
    
    file = open(input, 'r')
    lines = file.readlines()
    file.close()

    tokens_list = [line.split() for line in lines]
    for interval in intervals:
        elements = [tokens for tokens in tokens_list if int(tokens[0]) >= interval[0] and int(tokens[0]) <= interval[1]]
        file = open(str(interval[0]) + '-' + str(interval[1]),'w')
        for element in elements:
            file.write('\t'.join(element) + '\n')
        file.close()


def statistics(input, output='statistics.log'):

    import os
    os.system('rm ./statistics -r')
    os.system('mkdir ./statistics')
    os.system('rm ./dictionaries -r')
    os.system('mkdir ./dictionaries')

    file = open(input, 'r')
    lines = file.readlines()
    file.close()

    tokens_list = [line.split('\t')[:-1] for line in lines]
    frequency_list = Counter()
    wrongs_list = Counter()

    for label in LABELS:
        frequency_list[label] = 0

    LABELS_set = set(LABELS)

    '''Generating statistics: rights'''
    for tokens in tokens_list:
        if 'id=' in tokens[-1]:
            intersection = set(tokens[-3:]).intersection(LABELS_set)    
        else:
            intersection = set(tokens[-2:]).intersection(LABELS_set)
        #intersection = set(tokens).intersection(LABELS_set)
        if len(intersection) == 1:
            if 'id=' in tokens[-1]:
                '''Found a miss'''
                key = intersection.pop() + ' ' + tokens[-1][:3]
                if key not in wrongs_list.keys():
                    wrongs_list[key] = 1
                else:
                    wrongs_list[key] += 1
                '''Writing statistics files'''
                file = open('statistics/'+key, 'a')
                file.write('\t'.join(tokens)+'\n')
                file.close()
            else:
                key = intersection.pop()
                if key == tokens[-1]:
                    '''Writing statistics files'''
                    file = open('statistics/'+key, 'a')
                    file.write('\t'.join(tokens)+'\n')
                    file.close()
                    '''Writing dictionary files'''
                    if key in ['ac', 'co', 'ner', 'si']:
                        file = open('dictionaries/'+key, 'a')
                        file.write('\t'.join(tokens[:-1])+'\n')
                        file.close()
                    frequency_list[key] += 1
        elif len(intersection) == 2:
            if 'id=' in tokens[-1]:
                key = [intersection.pop(), intersection.pop(),'id=']
            else:
                key = [intersection.pop(), intersection.pop()]
            key.sort()
            key = '\t'.join(key)
            
            '''Writing statistics files'''
            file = open('statistics/'+key, 'a')
            file.write(' '.join(tokens) + '\n')
            file.close()
            '''Writing dictionary files'''
            if key in ['co\tner', 'in\tsi', 'ner\tsi']:
                file = open('dictionaries/'+key, 'a')
                file.write('\t'.join(tokens[:-2])+'\n')
                file.close()
            if key not in frequency_list.keys():
                frequency_list[key] = 1
            else:
                frequency_list[key] += 1

    '''Printing the statistics'''
    string = '{KEY:<25}\t{VALUE:<15}\n'
    print string.format(KEY="LABEL", VALUE="FREQUENCY")
    print string.format(KEY="-----", VALUE="---------")
    print string.format(KEY="RIGHTS", VALUE="")
    print string.format(KEY="-----", VALUE="---------")
    for i, j in frequency_list.most_common():
        print string.format(KEY=i, VALUE=j)
    print string.format(KEY="-----", VALUE="---------")
    print string.format(KEY="MISSES", VALUE="")
    print string.format(KEY="-----", VALUE="---------")
    for i, j in wrongs_list.most_common():
        print string.format(KEY=i, VALUE=j)


if __name__ == '__main__':

    filter_file('corrected_unknown_words_18_10.txt', 'filtrado.txt')
    statistics('filtrado.txt')
    #cria_grupos('corrected_unknown_words_sandra_magali_Final.txt', [(1009, 8229), (100, 999), (10, 99), (3, 9)])
