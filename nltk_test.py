### https://www.nltk.org/index.html
import nltk
### tag https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

sentence = 'formulation of 1580'

sentence = 'sales of 1580'

sentence = 'best eb in ov153'
sentence = 'product with highest percent of 1580 and J02B4'

tokens = nltk.word_tokenize(sentence)

print(tokens)

tagged = nltk.pos_tag(tokens)


#print(tagged[0:6])

print(tagged)