"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``English``
"""

# NP noun phrase pattern
NP = [
  [{"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "DET", "OP": "?"}, {"TAG": "VBG"}, {"POS": "NOUN"}],
]

# PP preposition phrase pattern
PP = [
  [{"TAG": "IN"}, {"POS": "DET"}, {"POS": "NOUN", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "PRP", "DEP": "pobj"}],
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
