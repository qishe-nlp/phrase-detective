from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    "Mi marido es el único que se presenta todos los años voluntario",
    "Y yo creo que lo mejor sería que fuéramos solo amigos",
    "3 nada más?",
    "Haz el ridículo tú sola!",
    "Pues a nosotras nos han entrado en nuestra casa a robar porque está el portal todo el santo día abierto!",
    "Ahora tienen que introducir un código secreto de 4 dígitos",
    "Bueno, por lo menos no se han llevado nada",
    "Pues que ha llegado el presidente de la comunidad y amparándose en no sé qué párrafo de no sé qué artículo",
    "Al primero B por el aire acondicionado",
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
  #spacy.displacy.serve(docs, style="dep")

