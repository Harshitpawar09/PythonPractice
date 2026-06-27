import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt');
nltk.download('stopwords');
nltk.download('wordnet')
nltk.download('punkt_tab')

text = 'Students are learning Python for AI and Machine Learning in Bhopal!'

tokens = word_tokenize(text.lower())
print('Tokens:', tokens)
stop = set(stopwords.words('english'))
filtered = [w for w in tokens if w not in stop and w.isalpha()]
print('after stopword removal:', filtered)
lemma = WordNetLemmatizer()
final = [lemma.lemmatize(w) for w in filtered]
print('after lemmatisation:', final)
from sklearn.feature_extraction.text import TfidfVectorizer
docs = ['Python is great for data science', 'machine learning is amazing','AI is the future of technology']
tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(docs)
print('TF-IDF shape:', matrix.shape)
print('Feature names:', tfidf.get_feature_names_out())