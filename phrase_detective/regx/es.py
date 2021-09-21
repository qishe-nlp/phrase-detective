"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``Spanish``
"""


# NP noun phrase pattern
BASE_PPP = [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN", "DEP": {"IN": ["nmod"]}}]
NP = [
  [{"POS": "DET", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": {"IN": ["NOUN", "PRON"]}}] + BASE_PPP,
  [{"POS": "DET", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"DEP": "advmod", "OP": "?"}, {"POS": "ADJ", "DEP": "amod"}],
  [{"POS": "DET", "OP": "+"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"LOWER": {"NOT_IN": ["que", "qué"]}, "POS": {"IN": ["PRON", "PROPN"]}}],
  [{"POS": {"IN": ["DET", "PRON"]}}, {"POS": "ADJ", "DEP": "nsubj"}, {"POS": "ADJ", "OP": "?", "DEP": "amod"}],
  [{"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "NOUN"}, {"POS": "PRON","MORPH": {"IS_SUPERSET": ["Poss=Yes"]}}],
]


# VERB Knowledge pattern
VERB = [
  [{"POS": "VERB"}],
  [{"POS": "AUX"}],
]

VERB_PASSIVE = [
  [{"LEMMA": "ser"}, {"TAG": {"REGEX": "VERB_.*Tense=Past|VerbForm=Part"}}],
  [{"LOWER": "se", "DEP": "obj"}, {"TAG": {"REGEX": "VERB_.*"}}],
]


es_regx = {
  "verb": VERB,
  "verb_passive": VERB_PASSIVE,
  "np": NP,
}
