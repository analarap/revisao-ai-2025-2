import nltk
from nltk.util import ngrams
from collections import Counter

# nltk.download("all")

# Etapa 1: Definição do Corpus
corpus = "O Senhor Ministro Dias Toffoli relatou o caso. A decisão foi unânime. O caso envolvia um recurso em habeas corpus. O julgamento ocorreu no STF"

# Etapa 2: Tokenizar o Corpus
tokens = nltk.word_tokenize(corpus.lower()) # Importante adicionar o método lower para não diferenciar palavras iguais que iniciam com Maiusculo e minusculo

# Etapa 3: Criar modeo n-grama
bigrams = list(ngrams(tokens, 2))
frequencias = Counter(bigrams) # Serve para ver qual a frequência daquele bigrama no vetor

print(bigrams)
print(frequencias)
print(frequencias.most_common(1)) # Pega um bigrama mais comum

# Etapa 4: 