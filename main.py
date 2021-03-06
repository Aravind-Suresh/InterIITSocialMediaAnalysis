import sys
import json
import re

from tweet import *
from wordProc import *

# Ensuring correct arguments
if not len(sys.argv) == 4:
	print "Usage : %s <Twitter app credentials> <input file> <number of tweets>" % sys.argv[0]
	sys.exit()

if __name__ == '__main__':
    with open(sys.argv[1]) as data_file:
        app = json.load(data_file)

    fin = open(sys.argv[2], 'r')
    count = eval(sys.argv[3])
    lines = fin.readlines()

    # Container to store paras
    results = []
    temp = ''
    te = TwitterExtract(app)
    if len(lines) == 1:
		lines.append('')
    for line in lines:
		line = line.strip()
		if line == '':
			temp = re.sub('[^a-zA-Z0-9 ]', '', temp)
			temp = re.sub(' +', ' ', temp)
            # print temp
			keywords = extractKeywords(temp)
			# print keywords
			if not keywords[0] == '':
				obj = te.fetchData(keywords, count)
				obj = str(obj)
				obj=re.sub(r'[^\x00-\x7F]+','', obj)
				results.append(obj)
			temp = ''
		else:
			temp = temp + line

    print results
