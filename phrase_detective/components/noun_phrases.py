# -*- coding: utf-8 -*-
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from phrase_detective.lib import merge
from phrase_detective.regx import REGX


class NounPhraseRecognizer:
  """Customerized component to detect noun phrases in ``spacy.tokens.Doc`` object. The ``NP`` values are stored in ``doc._.noun_phrases``,

  Attributes:
    ext_name (str): customized extension field name
    matcher (spacy.mathcer.Matcher): Rule maker for detecting ``NP``
  """

  def __init__(self, nlp):
    """Initialize the pipeline component. The shared nlp instance is used to initialize the matcher.
    
    Args:
      nlp (spacy.Language): language environment
    """

    self.ext_name = "noun_phrases"
    self.matcher = Matcher(nlp.vocab)
    np_patterns = REGX[nlp.meta["lang"]]["np"]
    self.matcher.add("NP", np_patterns)

    if not Doc.has_extension(self.ext_name):
      Doc.set_extension(self.ext_name, default=[])

  def __call__(self, doc):
    """Apply the pipeline component on a ``Doc`` object and modify it if matches are found.

    Returns:
      Doc: with customized extension ``doc._.noun_phrases``
    """

    matches = self.matcher(doc)

    phrases = []
    ranges = [(start, end) for _, start, end in matches]
    refined_matches = merge(ranges)
    for start, end in refined_matches:
      np = Span(doc, start, end)
      phrases.append(np)
    doc._.noun_phrases = phrases
    return doc

  def __del__(self):
    """Remove customized extension ``doc._.noun_phrases``
    """
    if Doc.has_extension(self.ext_name):
      Doc.remove_extension(self.ext_name)

