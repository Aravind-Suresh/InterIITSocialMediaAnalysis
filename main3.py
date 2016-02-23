# Necessary modules imported
import numpy as np
import sys
from InstagramExtract import *

# Ensuring correct arguments
if not len(sys.argv) == 1:
	print "INSTAGRAM API DEMO"
	print "Usage : %s <Credentials> <input file> <number of tweets>" % sys.argv[0]
	sys.exit()

with open(sys.argv[1]) as data_file:
    cred = json.load(data_file)

ie = InstagramExtract(cred["instagram"])
data = ie.fetchData("zuckerberg", limit=5, maxPages=2)
print data
