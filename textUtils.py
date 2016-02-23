# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:11:02 2016
@author: rsk
"""

import nltk
import re
import string
import os
import math
from textblob import TextBlob as tb

import sys
import json
import re

from tweet import *
from wordProc import *

from nltk.stem.porter import PorterStemmer

import nltk
#from newspaper import Article
from nltk.stem.snowball import SnowballStemmer

stemmer = PorterStemmer()

def stem_tokens(tokens,stemmer):
    stemmed=[]
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    return pos

def removeQuotes(text):
    keywords=[]

    while text.find("(")!= -1:
        start = text.find("(")
        end  = text.find(")")
        quote = text[(start+1):(end)]
        splits = quote.split()

        if len(splits)==1:
            keywords.append(splits[0])
        elif len(splits)==2:
            keywords.append(splits[0] + splits[1])
        else:
            r=4

        keywords.append(quote)
        text = text[:(start-1)] + text[(end+1):]
        print text

    return keywords

def headKeywords(text):

    keywords=[]
    bikeywords=[]

    #Removing quotes

    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)

    for i in range(len(pos)-1):
        if pos[i][1]=='NNP':
            keywords.append(pos[i][0])

            if pos[i+1][1]=='NNP':
                bikeywords.append(pos[i][0]+pos[i+1][0])
    if pos[len(pos)-1][1]=="NNP":
        keywords.append(pos[len(pos)-1][0])

    return (bikeywords,keywords)

def preprocess(text,):
    text = text.translate(None,string.punctuation)
    return text

def splitParagraph(text):

    text = re.split('\n',text)
    para=[]

    for i in text:
        if i != '':
            para.append(i)

    return para

import googlesearch
from googlesearch import GoogleSearch

def getGoogleContent(query):
    contents=[]
    gs = GoogleSearch(query)

    for i in gs.top_results():
        contents.append(i['url'])

    return contents

#headF = True, textF = True
file = open(sys.argv[2],'r')
lines = file.read()

hd = lines
lines = re.sub(r'[^\x00-\x7F]+','', lines)
lines = preprocess(lines)

paras = splitParagraph(lines)
paraCount = len(paras)

lKeys = []
MIN_KEYWORD_COUNT = 0
for i in range(0, paraCount):
    ll = headKeywords(paras[i]); ll=ll[0]+ll[1]
    if len(ll) < MIN_KEYWORD_COUNT:
        u = getGoogleContent(paras[i])
        # for j in range(0, 4):
        #     article = Article(u[i])
        #     article.download()
        #     article.parse()
        #     article.nlp
        #
        # k = article.keywords
        # ll = k
    lKeys.append(ll)

with open(sys.argv[1]) as data_file:
    app = json.load(data_file)
count = eval(sys.argv[3])
te = TwitterExtract(app)

results = []

for keys in lKeys:
    if not len(keys) == 0:
        obj = te.fetchData(keys, count)
        results.append(obj)
	#print json.loads(obj[0])

with open(sys.argv[4] + "/out.json", 'w') as outfile:
	json.dump(results, outfile)
#fout.write(s)
#fout.close()

#print lKeys
#for keys in lKeys:
#	print ",".join(keys)
