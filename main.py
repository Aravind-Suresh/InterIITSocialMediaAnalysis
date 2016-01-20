from tweet import *
from keyword import *

import sys
import json
import re

if __name__ == '__main__':

    with open(sys.argv[1]) as data_file:
        app = json.load(data_file)

    fin = open(sys.argv[2], 'r')
    lines = fin.readlines()

    # Container to store paras
    results = []
    temp = ''
    for line in lines:
        if line == '\n':
            temp = re.sub('[^a-zA-Z0-9]', ' ', temp)
            temp = re.sub(' +', ' ', temp)
            keywords = extractKeywords(temp)
            results.append(fetchData(app, keywords, 1))
            temp = ''
        else:
            temp = temp + line
