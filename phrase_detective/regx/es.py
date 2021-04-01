"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``Spanish``
"""


# NP noun phrase pattern
NP = [
  [{"POS": "DET", "OP": "+"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ"}],
  [{"POS": "NOUN"}, {"POS": "ADJ"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "NUM"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
]

# PP preposition phrase pattern
PP = [
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "PROPN"}],
  [{"POS": "ADP"}, {"POS": "PRON"}],
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
