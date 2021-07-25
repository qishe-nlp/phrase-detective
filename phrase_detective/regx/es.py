"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``Spanish``
"""


# NP noun phrase pattern
NP = [
  [{"POS": "DET", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "ADP", "OP": "!"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN", "DEP": "nmod"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"DEP": "advmod", "OP": "?"}, {"POS": "ADJ"}],
  [{"POS": "DET", "OP": "+"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"LOWER": {"NOT_IN": ["que", "qué"]}, "POS": {"IN": ["PRON", "PROPN"]}}],
  [{"POS": {"IN": ["DET", "PRON"]}}, {"POS": "ADJ", "DEP": "nsubj"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "NOUN"}, {"POS": "PRON","MORPH": {"IS_SUPERSET": ["Poss=Yes"]}}],
]

# PP preposition phrase pattern
PP = [
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "DET", "OP": "?"}, {"POS": "PROPN"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "ADV", "LOWER": {"NOT_IN": ["no"]}}, {"POS": "ADP", "OP": "?"}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "PRON", "LOWER": {"NOT_IN": ["lo"]}}],
  [{"POS": "ADP", "LOWER": {"NOT_IN": ["de", "del", "a", "al"]}}, {"POS": "ADJ"}],
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
  "pp": PP,
  "np": NP,
}
