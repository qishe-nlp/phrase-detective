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
  sentence = "No puedo Juan porque es que tengo cita en el ginecólogo"
  #sentence = "Pues a nosotras nos han entrado en nuestra casa a robar porque está el portal todo el santo día abierto!"
  #sentence = "Señoras, enhorabuena por su elección! Este sistema de alarma consta de 3 sensores de movimiento"
  #sentence = "El qué?"
  #sentence = "Mete el código por favor"
  #sentence = "En vista de vuestra actitud, no me queda más remedio que convocar una junta extraordinaria de vecinos"
  #sentence = "Según el artículo 17 de la ley de propriedad horizontal párrafo 5"
  #sentence = "A mí se me está cayendo el pelo por el estrés"
  #sentence = "Ya estás otra vez con la acidez?"
  #sentence = "Esto es el colmo! También instalan alarmas sin mi permiso"
  #sentence = "No tengo yo otra cosa que hacer a estas alturas que ir de hetero por la vida"
  #sentence = "Que si quieres tirar 5 años de relación por la borda, que los tires"
  #sentence = "Hombre por favor! Que tengo a los niños durmiendo"
  #sentence = "No, 3 millones de pesetas por piso"
  #sentence = "Es que se ha puesto nerviosa y ha tratado de cortarse las venas con el abono de transporte"
  #sentence = "Haz el ridículo tú sola!"
  #sentence = "3 nada más?"
  #sentence = "Tranquilo que solo quería meterle el miedo en el cuerpo"
  #sentence = "Es ese tío de abajo que me pone enferma"
  #sentence = "Señoras por dios!"
  #sentence = "Le va a poner hielo al vino?"
  #sentence = "Mi marido es el único que se presenta todos los años voluntario"
  #sentence = "Y yo creo que lo mejor sería que fuéramos solo amigos"
  #sentence = "El baño está ahí al fondo a la derecha"
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
  sentence = "Bueno, por lo menos no se han llevado nada"
  sentence = "Pues que ha llegado el presidente de la comunidad y amparándose en no sé qué párrafo de no sé qué artículo"
  sentence = "Al primero B por el aire acondicionado"
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

