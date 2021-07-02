import nltk
from nltk.tokenize import  word_tokenize,sent_tokenize
from nltk.tokenize import  WordPunctTokenizer
from nltk.stem import PorterStemmer,WordNetLemmatizer

text="Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers,irrational numbers, geometrical magnitudes, etc., to all be treated as \"algebraic objects\". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itselfin a way which had not happened before."
#first tokenization

#word tokenization
word_tok=word_tokenize(text)
print(word_tok)

#sentence tokenization
sent_tok=sent_tokenize(text)
print(sent_tok)

#WordPunctTokenizer split all the punctuation
tokenizer=WordPunctTokenizer()
print(tokenizer.tokenize(text))

#second pos tagging
pos=nltk.pos_tag(word_tok)
print(pos)


#third steming and lemmatisation

stem=PorterStemmer()
lemm=WordNetLemmatizer()

for w in word_tok:
    print(w," : ",stem.stem(w)," : ",lemm.lemmatize(w))


