"""Define regular expression usage of ``spacy.matcher.Matcher`` for ``German``
"""

# VERB Knowledge pattern
DE_VERB = [
  [{"POS": "VERB"}],
  [{"TAG": "VAFIN"}],
  [{"TAG": "VAIMP"}],
  [{"TAG": "VAINF"}],
  [{"TAG": "VAPP"}],
  [{"TAG": "VMFIN"}],
  [{"TAG": "VMINF"}],
  [{"TAG": "VMPP"}],
  [{"TAG": "VVFIN"}],
  [{"TAG": "VMIMP"}],
  [{"TAG": "VMINF"}],
  [{"TAG": "VVIZU"}],
  [{"TAG": "VVPP"}],
]

