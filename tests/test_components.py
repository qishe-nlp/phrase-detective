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
  lang = "de"
  sentence = "Wo ist der nächste Supermarkt ?"

#  sentence = "Dieser gottverdammte fünfte Budenplatz."
#  sentence = "und Sie mehr auf der hellen Seite des Mondes,"
#  sentence = "Die Menschen da… die kommen vom anderen Ende der Welt."
#  sentence = "Das hatte zehn Hörner und sieben Häupter."
#  sentence = "Also, mein lieber Urban, was haben Sie für mich?"
#  sentence = "Der junge Hoflinger hat schwere Kost aufgefahren."
#  sentence = "Der Hoflinger war ein Sonderfall."
#  sentence = "Wir bauen Münchens Zukunft."
#  sentence = "Jetzt merkst du, was Gottes Hilfe wert ist."
#  sentence = "Ich garantiere für die Sicherheit von Mutter und Jungen."
#  sentence = "In der Pinakothek hab ich dich nicht gefunden."
#  sentence = "Du kennst doch einen Haufen Künstler, und ich würd… fragen…"
#  sentence = "Die erste bayrische Bierburg mit Platz für 6.000 Leut!"
#  sentence = "Das sind Leute vom Luggi."
#  sentence = "Dies ist ein Gedicht unseres verehrten Lehrers Nietzsche."
#  sentence = "Über Mensch und Tier"
#
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("nprecog")
  doc = nlp(sentence)
  nps = []
  for np in doc._.noun_phrases:
    nps.append(np.text)
  print(nps)
  assert len(nps) == 1
  assert nps[0] == "der nächste Supermarkt"


def test_pprecog():
  lang = "de"
  sentence = "Diese Katze liegt auf dem Tisch."

#  sentence = "und Sie mehr auf der hellen Seite des Mondes."
#  sentence = "Also, auf geht's!"
#  sentence = "Die Menschen da… die kommen vom anderen Ende der Welt." 
#  sentence = "Eine Insel, die zum deutschen Schutzgebiet gehört in der Südsee."
#  sentence = "Schauen Sie, die Wunde am Kopf Ihres Vaters…"
#  sentence = "Mit Gottes Hilfe schaffen wir das."
#  sentence = "Vater hat dir die Steigbügel gehalten. Jetzt hör auf mit dem Scheiß!"
#  sentence = "2.500 Mark sind geboten. 2.500 zum Ersten."
#  sentence = "3.000 Mark zum Ersten."
#  sentence = "Ich garantiere für die Sicherheit von Mutter und Jungen."
#  sentence = "Ich muss zu Frau und Kind. Hör auf, die Nacht ist jung."
#  sentence = "In Giesing?"
#  sentence = "Du hast es mit höheren Mächten zu tun, Maria."
#  sentence = "Das sind Leute vom Luggi."
#  sentence = "Für die wundervolle Fanny."
#  sentence = "Über Mensch und Tier"
#  sentence = "Eine Fügung des Schicksals, von mir aus auch das."
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("pprecog")
  doc = nlp(sentence)
  pps = []
  for pp in doc._.prep_phrases:
    pps.append(pp.text)
  print(pps)
  assert len(pps) == 1
  assert pps[0] == "auf dem Tisch"

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

