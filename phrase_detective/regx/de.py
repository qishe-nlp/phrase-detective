"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``German``
"""

# NP noun phrase pattern
NP = [
  [{"POS": "ADJ"}, {"POS": "ADV", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADJ"}, {"POS": "ADV", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "PART"}, {"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "DET"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADV"}],
]

# PP preposition phrase pattern
PP = [
  [{"POS": "ADP"}, {"POS": "DET"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "PROPN"}],
  [{"POS": "ADP"}, {"POS": "NOUN"}, {"POS": "DET"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "PRON"}, {"POS": "PRON"}],
  [{"POS": "ADP"}, {"POS": "PRON"}, {"POS": "ADP"}, {"POS": "PROPN"}],
  [{"POS": "ADP"}, {"POS": "PRON"}, {"POS": "ADP"}, {"POS": "PROPN"}],
  #[{"POS": "ADP"}, {"POS": "PRON"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "ADV"}],
  [{"POS": "ADP"}, {"POS": "ADV"}, {"POS": "ADV"}],
  [{"POS": "ADP"}, {"POS": "ADP"}, {"POS": "DET"}, {"POS": "NOUN"}],
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
