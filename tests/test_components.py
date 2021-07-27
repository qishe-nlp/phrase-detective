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

  sentence = "Das kann nur bedeuten, dass er mit der Kehlkopfgewebeprobe des Kronprinzen zurück aus San Remo."
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
  lang = "de"
  sentence = "Das kann nur bedeuten, dass er mit der Kehlkopfgewebeprobe des Kronprinzen zurück aus San Remo."
  sentence = "Prof. von Bergmann wird sie operieren. Aber der Professor ist leider nicht im Hause."
  sentence = "Niemand außer ihm und Prof. von Bergmann beherrscht diesen neuen Eingriff."
  sentence = "Sie werden also selbst Ihre Schulden über 137,10 Mark in Ihre Abarbeiten in der Stelung als Hilfswärterin."
  sentence = "Sie bekommen Verpflegung 3. Klasse. Dienst ist täglich von 4:30 Uhr bis 22 Uhr."
  sentence = "Sonntags von 3 bis 6 dienstfrei. Ausgang gibt es allerdings nur mit meiner schriftlichen Erlaubnis."
  sentence = "Ich hätte nie gedacht, dass Sie also zu den 99 Narren gehören,"
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

