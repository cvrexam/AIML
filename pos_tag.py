import nltk
from nltk.tokenize import word_tokenize as wt
from nltk import pos_tag as pt
nltk.download('averaged_perceptron_tagger')
p = "This is a sample sentence,showing off the stop words filtration."
w = wt(p)
ps = pt(w)
for w,tag in ps:
    print(f'{w}:{tag}')
