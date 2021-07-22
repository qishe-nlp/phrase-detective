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
  sentence = "Vicenta, has visto cómo está este mando a distancia?"
  sentence = "Estos ya no saben qué hacer para quitarse los viejos de encima"
  sentence = "Precioso día"
  sentence = "A mí tampoco, qué vergüenza!"
  sentence = "Llámame, que yo creo que los tíos estos que ha traído tu padre están haciendo lo que les da la gana"
  sentence = "La que lleva esto es mi novia y está trabajando y no me coge el teléfono"
  sentence = "Los que han roto la puerta"
  sentence = "Pues vaya guardián de perro!"
  sentence = "Se me ha ocurrido una idea super original para hablar con Fernando"
  sentence = "Ay madre que día llevo, dios de mi vida, qué cansancio"
  sentence = "Ay dios mío! Que nos han entrado en casa"
  sentence = "Lo mismo os violan que os matan a las 2"
  sentence = "Yo no sé cómo podéis vivir tranquilas en un primero"
  #sentence = "La desesperada se marchó sola."
  #sentence = "Los primeros son los más rápidos."
  #sentence = "Lo único importante es su literatura."
  #sentence = "Lo gracioso es que podemos dibujar hasta flores."
  #sentence = "No les hagas caso, son unos miserables."

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
  #sentence = "y me despierto cada día en medio de un huracán"
  sentence = "Para la hija del jefe lo que haga falta"

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

