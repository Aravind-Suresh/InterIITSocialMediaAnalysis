import sys
import json
import re

from tweet import *
from wordProc import *

if __name__ == '__main__':
    with open(sys.argv[1]) as data_file:
        app = json.load(data_file)

    fin = open(sys.argv[2], 'r')
    lines = fin.readlines()

    # Container to store paras
    results = []
    temp = ''
    te = TwitterExtract(app)
    for line in lines:
        if line == '\n':
            temp = re.sub('[^a-zA-Z0-9 ]', '', temp)
            temp = re.sub(' +', ' ', temp)
            # print temp
            keywords = extractKeywords(temp)
            print keywords
            obj = te.fetchData(keywords, 1)
            results.append(obj)
            temp = ''
        else:
            temp = temp + line

    print results
