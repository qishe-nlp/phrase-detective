"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``English``
"""

# NP noun phrase pattern
NP = [
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN", "OP": "?"}, {"POS": "NOUN", "DEP": "pobj"}],
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"TAG": "VBG", "OP": "*"}, {"POS": "NOUN"}],
  [{"POS": "ADJ", "OP": "+"}, {"POS": "NOUN"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "NOUN"}, {"POS": "NOUN"}],
  [{"POS": "PRON"}, {"POS": "ADJ", "DEP": "amod"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADV", "DEP": "advmod"}],
]

# PP preposition phrase pattern
PP = [
  [{"TAG": "IN"}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "IN"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}],
  [{"TAG": "IN"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADV", "DEP": "pcomp"}],
  [{"POS": "VERB", "OP": "!"}, {"TAG": "IN"}, {"TAG": "PRP", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"POS": "PROPN", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "CD"}, {"POS": "NOUN", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "CD", "DEP": "pobj"}],
]

# VERB Knowledge pattern
VERB = [
  [{"POS": "VERB"}],
  [{"TAG": "VB"}],
  [{"TAG": "VBZ"}],
  [{"TAG": "VBN"}],
  [{"TAG": "VBP"}],
  [{"TAG": "VBG"}],
  [{"TAG": "VBD"}],
]

VERB_PASSIVE = [
  [{"DEP": "aux", "OP": "?"}, {"POS": "AUX", "DEP": "auxpass"}, {"POS": "VERB"}],
]

en_regx = {
  "verb": VERB,
  "verb_passive": VERB_PASSIVE,
  "pp": PP,
  "np": NP,
}
