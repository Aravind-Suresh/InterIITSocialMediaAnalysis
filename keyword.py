from nltk import pos_tag, word_tokenize
import sys

sentence = sys.argv[1]
a = pos_tag(word_tokenize(sentence))
i=0
temp = ''

for i in xrange(0,len(a)):
   if (a[i][1] == 'NNP' and (a[i-1][1] == 'NNP' or i==0)):
       temp = temp + a[i][0]                            #NO SPACE IS ADDED WHILE COMBINING 2 SIMILAR WORKS AS THEY ARE MOST LIKELY TO BE A PART OF THE SAME WORD
   elif (a[i][1] == 'NNP' and (a[i-1][1] == 'NN' or i==0)):       #SO WHEN THEY ARE USED IN HASHTAGS THEY ARE COMBINED(eg. THE WORD SANJAY KUMAR BECOMES #SANJAYKUMAR)
       temp = temp + a[i][0]
   elif (a[i][1] == 'NNP' and a[i-1][1] != 'NNP'):
       temp = temp + ' ' + a[i][0]
   elif (a[i][1] == 'NN' and a[i-1][1] == 'NN'):
       temp = temp +  a[i][0]                          #NO SPACE IS ADDED WHILE COMBINING 2 SIMILAR WORKS AS THEY ARE MOST LIKELY TO BE A PART OF THE SAME WORD
   elif (a[i][1] == 'NN' and a[i-1][1] == 'NNP'):                 #SO WHEN THEY ARE USED IN HASHTAGS THEY ARE COMBINED(eg. THE WORD SANJAY KUMAR BECOMES #SANJAYKUMAR)
       temp = temp +  a[i][0]
   elif (a[i][1] == 'NN' and a[i-1][1] != 'NN'):
       temp = temp + ' ' + a[i][0]

text = temp.split(' ')
