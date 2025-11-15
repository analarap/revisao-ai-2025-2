# a palavra que podemos procurar no dicionario

import nltk
# nltk.download('wordnet')

lema = nltk.stem.WordNetLemmatizer()
texto = "I am nothing. I will never be anything. I cannot want to be anything. Apart from that, I have within me all the dreams in the world."

poema = lema.lemmatize(texto)
print(poema)