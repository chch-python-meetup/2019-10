
from nltk import word_tokenize, FreqDist, TweetTokenizer


from nltk.tokenize import RegexpTokenizer

import matplotlib.pyplot as plt

import operator

from collections import OrderedDict

tweet_tokenise = TweetTokenizer()

stop_list = ['[', ']', ',', '.', '(', ')', ';']

#tokenizer = RegexpTokenizer(r'\w+')

filename = 'Waitangi.txt'
#filename = 'Waitangi_M.txt'

file = open(filename)
raw = file.read()

tokens = tweet_tokenise.tokenize(raw)


#print (tokens)
#input('paused')

#tokens2 = tokenizer.tokenize(raw)

#tokens3 = [x.lower() for x in tokens2]

tokens3 = [x.lower() for x in tokens if x not in stop_list]

#print(tokens2)


print ('the total wordcount is:')
print (len(tokens3))


fdist = FreqDist(tokens3)

filtered_word_freq = dict((word, freq) for word, freq in fdist.items())
#print (filtered_word_freq)

sorted_word_freq = sorted(filtered_word_freq.items(), key=operator.itemgetter(1))

print (sorted_word_freq)

#sorted_word_freq.reverse()

sorted_dict = OrderedDict(sorted_word_freq)

plt.barh(range(len(sorted_dict)), list(sorted_dict.values()), align='center')
plt.yticks(range(len(sorted_dict)), list(sorted_dict.keys()))
plt.ylabel('word')
plt.xlabel('frequency')
plt.title('Frequency of words in the Treaty of Waitangi')
plt.show()