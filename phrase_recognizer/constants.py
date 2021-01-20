# NP noun phrase pattern
NP_EN = [
  [{"POS": "DET"}, {"POS": "ADJ"}, {"POS": "NOUN"}],
  [{"POS": "DET", "OP": "?"}, {"TAG": "VBG"}, {"POS": "NOUN"}],
]

NP_ES = [
  [{"POS": "DET", "OP": "+"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "NOUN"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "NOUN"}, {"POS": "ADJ"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NUM"}, {"POS": "NOUN"}],
]

NP_PATTERNS = {
  "en": NP_EN,
  "es": NP_ES
}


# PP preposition phrase pattern
PP_EN = [
  [{"TAG": "IN"}, {"POS": "DET"}, {"POS": "NOUN", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "PRP", "DEP": "pobj"}],
  [{"TAG": "IN"}, {"TAG": "CD", "DEP": "pobj"}],
]

PP_ES = [
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "NOUN"}],
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}, {"POS": "ADJ", "OP": "?"}],
  [{"POS": "ADP"}, {"POS": "DET", "OP": "?"}, {"POS": "PROPN"}],
  [{"POS": "ADP"}, {"POS": "PRON"}],
  [{"POS": "ADP"}, {"POS": "ADV"}],
]

PP_PATTERNS = {
  "en": PP_EN,
  "es": PP_ES
}

# VERB Knowledge pattern
VERB_PATTERN_EN = [
  [{"POS": "VERB"}],
  [{"TAG": "VB"}],
  [{"TAG": "VBZ"}],
  [{"TAG": "VBN"}],
  [{"TAG": "VBP"}],
  [{"TAG": "VBG"}],
  [{"TAG": "VBD"}],
]

VERB_PATTERN_ES = [
  [{"POS": "VERB"}],
  [{"POS": "AUX"}],
]

VERB_PATTERNS = {
  "en": VERB_PATTERN_EN,
  "es": VERB_PATTERN_ES
}

PASSIVE_PATTERN_EN = [
  [{"DEP": "aux", "OP": "?"}, {"POS": "AUX", "DEP": "auxpass"}, {"POS": "VERB"}],
]

PASSIVE_PATTERN_ES = [
  [{"LEMMA": "ser"}, {"TAG": {"REGEX": "VERB_.*Tense=Past|VerbForm=Part"}}],
  [{"LOWER": "se", "DEP": "obj"}, {"TAG": {"REGEX": "VERB_.*"}}],
]

PASSIVE_PATTERNS = {
  "en": PASSIVE_PATTERN_EN,
  "es": PASSIVE_PATTERN_ES
}

