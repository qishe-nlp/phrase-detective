"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``German``
"""

# NP noun phrase pattern
NP = [
  [{"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADP", "DEP": "mnr"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "+"}, {"POS": "NOUN"}],
  [{"POS": "PART"}, {"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}, {"POS": "DET"}, {"POS": "NOUN", "DEP": "ag"}],
  [{"POS": "NOUN"}, {"POS": "ADP"}, {"POS": "PROPN"}],
  [{"POS": "DET"}, {"POS": "NOUN", "DEP": "oa"}, {"POS": "NOUN", "DEP": "nk"}],
  [{"POS": "NOUN", "DEP": "nk"}, {"POS": "CCONJ", "DEP": "cd"}, {"POS": "NOUN", "DEP": "cj"}],
  [{"POS": "DET"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADJ", "OP": "?"}, {"POS": "PROPN"}],
  [{"POS": "ADJ", "OP": "+"}, {"POS": "NOUN"}],
  [{"POS": "ADJ", "OP": "+"}, {"POS": "PROPN"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NUM", "TAG": "CARD"}, {"POS": "NOUN"}, {"TAG": "ADJD", "OP": "?"}],
  [{"POS": "PRON", "DEP": "ag"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "NOUN", "DEP": "ag"}, {"POS": "NOUN"}],
  [{"POS": "PROPN", "DEP": "ag"}, {"POS": "NOUN"}],
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
  "np": NP,
}
