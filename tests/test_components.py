from spacy.language import Language
from phrase_detective import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer
from phrase_detective import PKG_INDICES
import spacy

@Language.factory("nprecog")
def create_np_parser(nlp: Language, name: str):
  return NounPhraseRecognizer(nlp) 

@Language.factory("pprecog")
def create_pp_parser(nlp: Language, name: str):
  return PrepPhraseRecognizer(nlp) 

@Language.factory("vkbrecog")
def create_vkb_parser(nlp: Language, name: str):
  return VerbKnowledgeRecognizer(nlp) 


def test_nprecog():
  lang = "es"
  sentence = "Voy a la playa."
  sentence = "Hay pocos errores aquí."
  sentence = "Póngame tres manzanas por favor."
  sentence = "¿Cuántos libros hay?"
  sentence = "¡Qué sorpresa!"
  sentence = "Me quedo en tu casa."
  sentence = "Los tres chicos son de mi barrio."
  sentence = "Me gusta tu caminar."
  sentence = "La desesperada se marchó sola."

  sentence = "Pedro es una persona amable."
  sentence = "Pedro es una gran persona."
  sentence = "La pobre chica española fue engañada."

  sentence = "Ella es mi compañera de clase."
  sentence = "Me gusta la biblioteca de mi universidad."
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("nprecog")
  doc = nlp(sentence)
  nps = []
  for np in doc._.noun_phrases:
    nps.append(np.text)
  print(nps)
  #assert len(nps) == 1
  #assert nps[0] == "der nächste Supermarkt"


def test_pprecog():
  lang = "es"
  sentence = "Es un libro de chino."
  sentence = "Quiero un café con leche."
  sentence = "Voy al gimnasio esta tarde."
  sentence = "A mi primo, le gusta leer libros."

  sentence = "Eres uno de nosotros."
  sentence = "No quiero nada de ti."
  
  sentence = "Un hombre salió de entre la gente."
  sentence = "Perdió la guerra por ambicioso."

  sentence = "El Gobierno aún tiene por delante una difícil tarea."
  sentence = "Es un paso por delante de la evolución de la tecnología."

  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("pprecog")
  doc = nlp(sentence)
  pps = []
  for pp in doc._.prep_phrases:
    pps.append(pp.text)
  print(pps)
  #assert len(pps) == 1
  #assert pps[0] == "auf dem Tisch"

def test_vkbrecog():
  lang = "de"
  sentence = "Diese Katze spielt auf dem Tisch."
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("vkbrecog")
  doc = nlp(sentence)

  for v in doc._.verbs:
    print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))
  for pp in doc._.passive_phrases:
    print(pp.text)
  for vp in doc._.verb_phrases:
    print(vp)

