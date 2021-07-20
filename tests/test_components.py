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
  lang = "en"
  #sentence = "Those people are so friendly!"
  #sentence = "The river is deeper after it rains."
  #sentence = "An enormous tree stands on the riverbank."
  #sentence = "The very tall consultant is saying something."
  #sentence = "Unmarried men are a rare species these days."
  #sentence = "Fresh water is a precious resource in Saudi Arabia."

  #sentence = "A tennis ball is a ball for playing tennis."
  #sentence = "Tennis shoes are shoes for playing tennis."

  #sentence = "This isn’t anything important."
  #sentence = "He wanted to get someone reliable to help in this work."

  #sentence = "People here know each other."
  #sentence = "It had been fine the day before."

  #sentence = "He is a student of astronomy."
  sentence = "Even a small rise in interest rates would hurt borrowers."
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
  lang = "en"
  sentence = "Don’t walk on the grass."
  sentence = "After the interview, they phoned the police."
  sentence = "We saw a girl with a small dog."
  sentence = "We saw a girl with small dogs."

  sentence = "And for me, I feel it's the key way to keep moving forward."

  sentence = "He looked at me from behind the tree."
  sentence = "I can't see you until after lunch."
  sentence = "Just come through here and I ’ll show you where the problem is."
  sentence = "Many of these treatments were used until quite recently."


  #sentence = "They left just after six о'clock."
  sentence = "There will be a concert on New Year's Day."
  sentence = "Typhoons seldom come in winter."
  sentence = "The short video spread quickly in China."

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

