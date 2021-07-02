import spacy


nlp = spacy.load('en_core_web_sm')
text=nlp("Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers,irrational numbers, geometrical magnitudes, etc., to all be treated as \"algebraic objects\". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itselfin a way which had not happened before.")

#sentence tokenization
for s in text.sents:
    print(s)

#word tokenization
for s in text:
    print(s)

#POS TAGGING
for w in text:
    print(w," : ",w.pos_," : ",w.tag_)

#spacy.explain('DT')

#stem and lemm
for w in text:
    print(w.text," : ",w.lemma_)