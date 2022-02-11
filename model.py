# 1. Library imports
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords_En = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()
# Modèle + Matrice de fonctionnalités TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english',max_df=0.7)

# 2. Cleaning news
def text_cleaning(news):
    news = "".join([word.lower() for word in news if word not in string.punctuation])
    tokens = word_tokenize(news)
    news = " ".join([ps.stem(word) for word in tokens if word not in stopwords_En])
    # Return a list of words
    return news