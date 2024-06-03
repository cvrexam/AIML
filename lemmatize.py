import nltk
from nltk.stem import WordNetLemmatizer
from nltk import wordnet
# Download wordnet resource (only needed once)
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ["cats", "running", "jumping"]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print(lemmatized_words)  # Output: ['cat', 'run', 'jump']