import nltk
import nltk.stem.snowball
from nltk.corpus import stopwords

nltk.download('punkt_tab')

# radicalização serve para generalizar uma palavra
texto = "Não sou nada. Nunca serei nada. Não posso querer ser nada. À parte isso, tenho em mim todos os sonhos do mundo."

palavras = nltk.word_tokenize(texto, language='portuguese')
snowballStem = nltk.SnowballStemmer('portuguese')

stop_words = stopwords.words('portuguese')
palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]

print('PALAVRAS FILTRADAS: ')
for palavra in palavras_filtradas:
    radical = snowballStem.stem(palavra)
    print(radical)

print('\nPALAVRAS NORMAIS: ')    
for palavra in palavras:
    radical = snowballStem.stem(palavra)
    print(radical)