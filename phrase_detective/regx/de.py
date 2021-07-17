"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``German``
"""

# NP noun phrase pattern
NP = [
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "PART"}, {"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "DET"}, {"POS": "NOUN", "DEP": "ag"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADV", "TAG": "ADV", "OP": "?"}],
  [{"POS": "ADJ"}, {"POS": "NOUN"}],
]

# PP preposition phrase pattern
PP = [
  [{"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}, {"POS": "DET"}, {"POS": "NOUN", "DEP": "ag"}],
  [{"POS": "ADP"}, {"POS": "DET"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "PRON"}],
  [{"POS": "ADP"}, {"POS": "ADV"}],
]

# TODO: VERB Knowledge pattern
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

de_regx = {
  "verb": VERB,
  "verb_passive": VERB_PASSIVE,
  "pp": PP,
  "np": NP,
}
