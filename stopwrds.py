import nltk
nltk.download('punkt')
from nltk.corpus import stopwords as sw
from nltk.tokenize import word_tokenize as wt
p = "This is a sample sentence,showing off the stop words filtration."
print(p)
nltk.download('stopwords')
swrds = sw.words('english')
twrds = wt(p)
sw = []
for w in twrds:
    if w not in swrds:
        sw.append(w)
print(twrds)
print(sw)
