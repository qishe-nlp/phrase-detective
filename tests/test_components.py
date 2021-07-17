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
  #sentence = "Die Komplemente werden in Komplementenklasen eingeteilt."
  #sentence = "Wir hatten ein sehr schönes Zimmer im Garden Block mit Blick aufs Meer."
  #sentence = "Seine diesjährige Ernte liefert eine sehr elegante Tasse."
  #sentence = "Mai ist für alle Menschen der Tag des Widerstands gegen Ausbeutung und Unterdrückung."
  #sentence = "Wie der Zug vorüber war, wurde er sich erst seiner Angst bewusst."
  #sentence = "Zwischen Berlin und Neubrandenburg ist der Zug wegen eines Defektes stehen geblieben."
  #sentence = "Eine Frau in den Siebzigern konnte auf ihrem linken Auge nicht sehen."
  #sentence = "Sie können Markus Klepper auch gerne anrufen, wenn Sie ganz konkrete Fragen haben."
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
  #sentence = "Ziel war es die Partner aus Übersee und die nationale Kirche ins Gespräch zu bringen."
  #sentence = "Zu Beginn des 19. Jh. wurde die Postkutsche durch Postautos abgelöst."
  #sentence = "Dabei ist uns auch wichtig, dass sich die Eltern aktiv an der Gestaltung der Schule beteiligen."
  #sentence = "Die Mitgliederversammlung werden von einem Mitglied des Vorstandes geleitet."
  #sentence = "Wie können Sie zu Ihm kommen?"
  #sentence = "Dann wurde ein Nachfolgekurs angeboten und für mich war die Teilnahme daran schon fast selbstverständlich."
  #sentence = "Dabei handelt es sich um Sendungen bis zu einem Gewicht von drei Kilogramm."
  #sentence = "Eine Vielzahl an Gebäuden wurde schwer beschädigt und die Bevölkerung ging bis auf die Hälfte zurück."
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

