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

  sentence = "qué tal doña concha?"
  sentence = "Ten cuidado bonito! No te vayas a tropezar y te rompes los dientes contra un banco"
  sentence = "Yo tengo que hacer ejercicio, me paso el día sentado"
  sentence = "Pero tú te crees que te voy a dejar en mi casa solo?"
  sentence = "Hombre claro, las lesiones son mayores pero bueno, para esto está el seguro, no?"
  sentence = "Ay pobrecito, yo lo veo hecho polvo"
  sentence = "Y la pequeña la tengo con depresión porque la dejó el marido y además con una niña de 6 meses"
  sentence = "Y mi marido en paro. Ahora está haciendo un cursillo de esos de reciclaje pero yo le sigo viendo la misma cara de amargura"
  sentence = "Si es que yo llego aquí y os veo a vosotros tan guapos y tan felices y empezando una vida juntos"
  sentence = "Encima voy a ser yo el malo de la película!"
  sentence = "Y ahora noto como...como como un poco de angustia y me cuesta respirar pero es de ilusión"
  #sentence = "Y hacemos queso de cabra y plantamos tomates"
  #sentence = "Que hay junta de vecinos?"
  #sentence = "Bueno, el hecho es que no tenemos seguro de responsabilidad civil y hay que pagarle los días de baja"
  sentence = "O mejor, se lo voy a decir a mi madre que venga un par de veces por semana"
  sentence = "Hombre pues un poco de pinta sí que tienes, mira"
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
  #sentence = "you are in touch with the very center of our planet,"
  #sentence = "because it's literally how we find our way across the face of the Earth."
  #sentence = "and we use compasses to find our way north because of that fact."
  #sentence = "Just come through here and I ’ll show you where the problem is."
  #sentence = "There will be a concert on New Year's Day."
  #sentence = "After the interview, they phoned the police."

  sentence = "Pero tú te crees que te voy a dejar en mi casa solo?"
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

