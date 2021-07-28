"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``English``
"""

# NP noun phrase pattern
EXCLUDED_PREP = ["to", "into", "out", "than"]
BASE_PPP_1 = [{"POS": "ADP", "LOWER": {"NOT_IN": EXCLUDED_PREP}}, {"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN", "OP": "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "pobj"}]
BASE_PPP_2 = [{"POS": "ADP", "LOWER": {"NOT_IN": EXCLUDED_PREP}}, {"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"TAG": "VBG", "OP": "?"}, {"POS": "NOUN", "OP": "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "pobj"}]
BASE_PPP_3 = [{"POS": "ADP", "LOWER": {"NOT_IN": EXCLUDED_PREP}}, {"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"TAG": "PRP$", "OP": "?"}, {"POS": "NOUN", "OP": "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "pobj"}]

NP = [
  [{"POS": "DET", "OP": "?"}, {"POS": "NOUN"}, {"POS": "PART", "TAG": "POS"}, {"POS": "NOUN"}],
  [{"POS": "ADJ", "OP": "?"}, {"POS": "NOUN"}, {"POS": "CCONJ"}, {"POS": "ADJ", "OP": "?"}, {"POS": "NOUN", "DEP": "conj"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}] + BASE_PPP_1,
  [{"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"POS": "NUM", "OP": "?"},{"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}] + BASE_PPP_2,
  [{"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"POS": "NUM", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}] + BASE_PPP_3,
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}],
  [{"POS": "DET"}, {"POS": "ADV", "OP": "?"}, {"TAG": "VBG", "OP": "*"}, {"POS": "NOUN"}],
  [{"POS": "DET", "OP": "?"}, {"POS": "NOUN", "DEP": "compound"}, {"POS": "NOUN"}],
  [{"POS": "PRON", "LOWER": {"NOT_IN": ["what, which"]}}, {"POS": "ADJ", "OP": "*"}, {"POS": "NOUN"}],
  [{"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "+"}, {"POS": "NOUN"}],
  [{"POS": "PRON"}, {"POS": "ADJ", "DEP": "amod"}],
]

# PP preposition phrase pattern
EXCLUDED_PREP = ["of", "to", "into", "out", "than", "like"]
BASE_PNP = [{"POS": "DET", "OP": "?"}, {"POS": "ADV", "OP": "?"}, {"POS": "ADJ", "OP": "?"}, {"POS": {"IN": ["NOUN", "PROPN"]}, "DEP": "pobj"}]
PP = [
  [{"LOWER": "between"}] + BASE_PNP + [{"LOWER": "and"}] + BASE_PNP,
  [{"LOWER": "from"}] + BASE_PNP  + [{"LOWER": "to"}] + BASE_PNP,
  [{"LOWER": "as"}, {"POS": {"IN": ["ADV", "ADJ"]}}, {"LOWER": "as"}, {"POS": {"IN": ["ADJ", "PROPN"]}}],
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}] + BASE_PNP + [{"TAG": "IN"}] + BASE_PNP,
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}] + BASE_PNP, 
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}] + [{"TAG": "IN"}] + BASE_PNP,
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}, {"POS": "ADV", "OP": "?"}, {"POS": "ADV", "DEP": "pcomp"}],
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}] + BASE_PNP, 
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}] + [{"TAG": "CD"}] + BASE_PNP,
  [{"TAG": "IN", "LOWER": {"NOT_IN": EXCLUDED_PREP}}, {"TAG": "CD", "DEP": "pobj"}],
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
