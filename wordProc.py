from nltk import pos_tag, word_tokenize
import sys

def extractKeywords(sentence):
    a = pos_tag(word_tokenize(sentence))
    i=0
    temp = ''

    for i in xrange(0,len(a)):
        if (a[i][1] == 'NNP' and (a[i-1][1] == 'NNP' or i==0)):
            temp = temp + a[i][0]
        elif (a[i][1] == 'NNP' and (a[i-1][1] == 'NN' or i==0)):
            temp = temp + a[i][0]
        elif (a[i][1] == 'NNP' and a[i-1][1] != 'NNP'):
            temp = temp + ' ' + a[i][0]
        elif (a[i][1] == 'NN' and a[i-1][1] == 'NN'):
            temp = temp +  a[i][0]
        elif (a[i][1] == 'NN' and a[i-1][1] == 'NNP'):
            temp = temp +  a[i][0]
        elif (a[i][1] == 'NN' and a[i-1][1] != 'NN'):
            temp = temp + ' ' + a[i][0]

    keys = temp.split(' ')
    return keys
