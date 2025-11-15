import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# -----------------------------
#  TEXTOS
# -----------------------------
texto_pt = "Não sou nada. Nunca serei nada. Não posso querer ser nada. À parte isso, tenho em mim todos os sonhos do mundo."
texto_en = "I am nothing. I will never be anything. I cannot want to be anything. Apart from that, I have within me all the dreams in the world."

# -----------------------------
#  TOKENIZAÇÃO + STOPWORDS
# -----------------------------
palavras = nltk.word_tokenize(texto_pt, language="portuguese")
stop = set(stopwords.words("portuguese"))
filtradas = [p for p in palavras if p.lower() not in stop]

# -----------------------------
#  RADICALIZAÇÃO (STEMMER)
# -----------------------------
stemmer = SnowballStemmer("portuguese")
radicais = [stemmer.stem(p) for p in filtradas]

# -----------------------------
#  LEMATIZAÇÃO (INGLÊS)
# -----------------------------
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(p) for p in nltk.word_tokenize(texto_en)]

# -----------------------------
#  RESULTADOS
# -----------------------------
print("\nPALAVRAS FILTRADAS:", filtradas)
print("RADICAIS:", radicais)
print("\nLEMAS (inglês):", lemmas)
