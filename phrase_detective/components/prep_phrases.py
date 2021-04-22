# -*- coding: utf-8 -*-
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from phrase_detective.lib import merge
from phrase_detective.regx import REGX


class PrepPhraseRecognizer:
  """Customerized component to detect noun phrases in ``spacy.tokens.Doc`` object. The ``PP`` values are stored in ``doc._.prep_phrases``.
  
  Attributes:
    ext_name (str): customized extension field name
    matcher (spacy.mathcer.Matcher): Rule maker for detecting ``PP``

  """

  def __init__(self, nlp):
    """Initialize the pipeline component. The shared nlp instance is used to initialize the matcher, which detects POS, TAG, DEP.

    Args:
      nlp (spacy.Language): language environment
    """

    self.ext_name = "prep_phrases"
    self.matcher = Matcher(nlp.vocab)
    pp_patterns = REGX[nlp.meta["lang"]]["pp"]
    self.matcher.add("PP", pp_patterns)

    if not Doc.has_extension(self.ext_name):
      Doc.set_extension(self.ext_name, default=[])
    

  def __call__(self, doc):
    """Apply the pipeline component on a Doc object and modify it if matches are found.
    
    Returns:
      Doc: with customized extension ``doc._.prep_phrases``
    """

    matches = self.matcher(doc)

    phrases = []
    ranges = [(start, end) for _, start, end in matches]
    refined_matches = merge(ranges)
    for start, end in refined_matches:
      if doc[start].text not in ['of', 'to', 'a']: # TODO: It is bad
        pp = Span(doc, start, end)
        phrases.append(pp)
    doc._.prep_phrases = phrases
    return doc

  def __del__(self):
    """Remove customized extension ``doc._.prep_phrases``
    """
    if Doc.has_extension(self.ext_name):
      Doc.remove_extension(self.ext_name)
