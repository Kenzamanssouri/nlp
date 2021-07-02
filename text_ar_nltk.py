import nltk
from nltk.tokenize import  word_tokenize,sent_tokenize
from nltk.tokenize import  WordPunctTokenizer
from nltk.stem import PorterStemmer,WordNetLemmatizer

text_ar = "ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل "

#first tokenization

#word tokenization
word_tok_ar=word_tokenize(text_ar)
print(word_tok_ar)

#sentence tokenization
sent_tok_ar=sent_tokenize(text_ar)
print(sent_tok_ar)

#WordPunctTokenizer split all the punctuation
tokenizer=WordPunctTokenizer()
print(tokenizer.tokenize(text_ar))


#second pos tagging
pos=nltk.pos_tag(word_tok_ar)
print(pos)


#third steming and lemmatisation

stem=PorterStemmer()
lemm=WordNetLemmatizer()

for w in word_tok_ar:
    print(w," : ",stem.stem(w)," : ",lemm.lemmatize(w))