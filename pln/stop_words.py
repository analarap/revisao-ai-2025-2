import nltk
from nltk.corpus import stopwords

texto = "Não sou nada. Nunca serei nada. Não posso querer ser nada. À parte isso, tenho em mim todos os sonhos do mundo."

sentencas = nltk.sent_tokenize(texto, language='portuguese')

palavras = nltk.word_tokenize(texto, language='portuguese')

stop_words = set(stopwords.words('portuguese'))
palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]
print("Palavras filtradas:", palavras_filtradas)
