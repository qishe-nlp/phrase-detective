from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    "Es que esto es un dineral para uno solo",
    "Cómo me alegro de que estés otra vez en casa, cariño",
    "Oye Chema, me puedo ir con vosotros esta noche?",
  ]

  #sens = []
  lang = "es"
  nlp = spacy.load(PKG_INDICES[lang])
  docs = []
  for sentence in sens:
    doc = nlp(sentence)
    for t in doc:
      print("{}: {} {} {} {}".format(t.text, t.pos_, t.morph, t.tag_, t.dep_))
    print()
    docs.append(doc)
  spacy.displacy.serve(docs, style="dep")

