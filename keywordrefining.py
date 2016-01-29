import nltk
from newspaper import Article
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")


from googlesearch import GoogleSearch

def getGoogleContent(query):
    contents=[]
    gs = GoogleSearch(query)

    for i in gs.top_results():
        contents.append(i['url'])

    return contents

url = []
keyword = ['']
newkey = ['']

url = getGoogleContent('Obama gets tough with Pak')

for i in xrange(0,3):
          article = Article(url[i])
          article.download()
          article.parse()
          article.nlp
	  k=article.keywords
	  for j in xrange(0,len(k)-1) :
		temp=stemmer.stem(k[j])
		k[j]=temp
          print(k)

#counter(newkey)
