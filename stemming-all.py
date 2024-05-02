from nltk.stem import PorterStemmer, LancasterStemmer,SnowballStemmer
from nltk.tokenize import word_tokenize as wt
p = "This is a sample sentence,showing off the stop words filtration."
ps = PorterStemmer()
ls = LancasterStemmer()
sb = SnowballStemmer(language='english')
twrds = wt(p)
for w in twrds:
    print(w, " : ", ps.stem(w))
print("****** ls *******")
for w in twrds:
    print(w, " : ", ls.stem(w))
print("****** sb *******")
for w in twrds:
    print(w, " : ", sb.stem(w))
