import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
 
document = 'Our project is based on machine learning, it\'s implementation will be done by using python.'
sentences = nltk.sent_tokenize(document)
data = []   
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))
for w in data:
	if 'VB' in w[1]:
		print(w)


'''# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
# ps = PorterStemmer()
# text = 'i love python language and i am a pythoner doing pythoning with python'
# word = word_tokenize(text)
# for w in word:
# 	print(ps.stem(w))'''


'''# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# text = 'he is a boy and he likes mango juice but he hates brinjle.'
# stop_words = set(stopwords.words('english'))
# print(stop_words)
# words = word_tokenize(text)
# f_sent = []
# for w in words:
# 	if w not in stop_words:
# 		f_sent.append(w)
# print(f_sent)'''


'''# from nltk.tokenize import sent_tokenize, word_tokenize
# text = 'he is a boy. he likes apple'
# print(sent_tokenize(text))
# print(word_tokenize(text))'''