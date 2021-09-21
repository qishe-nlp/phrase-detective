from spacy.language import Language
from phrase_detective import NounPhraseRecognizer, VerbKnowledgeRecognizer
from phrase_detective import PKG_INDICES
import spacy

@Language.factory("nprecog")
def create_np_parser(nlp: Language, name: str):
  return NounPhraseRecognizer(nlp) 

@Language.factory("vkbrecog")
def create_vkb_parser(nlp: Language, name: str):
  return VerbKnowledgeRecognizer(nlp) 


def test_nprecog():
  lang = "en"

  sentence = "So many of our brothers and sisters"
  sentence = "and our sons and brothers, husbands and fathers"
  sentence = "How could you contemplate such ruin and disappointment to yourself"
  sentence = "Over the coming weeks and months, you will all bear witness"
  sentence = "to conceal your infatuation for another man's wife."
  sentence = "I'm sure all the kids' dads love her too."
  sentence = "I rather like what I've seen of her. What, the shopkeeper's daughter?"
  sentence = "500 pages of instructions."
  sentence = "We've received a copy of a telegram"
  sentence = "With a nasty dose of the horrors when she sits on a horse."
  sentence = "She believes the people of Britain will help to accomplish it."
  sentence = "She's had a bit of a nervous breakdown."
  sentence = "she believes the country has to change from top to bottom,"
  sentence = "As a young woman, she applied for a job as a food research chemist"

  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("nprecog")
  doc = nlp(sentence)
  nps = []
  for np in doc._.noun_phrases:
    nps.append(np.text)
  print(nps)
  #assert len(nps) == 1
  #assert nps[0] == "der nächste Supermarkt"


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

