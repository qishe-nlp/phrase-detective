# -*- coding: utf-8 -*-
from spacy.tokens import Doc, Span
from spacy.language import Language 
from importlib import import_module


class NounPhraseRecognizer:
  """Customerized component to detect noun phrases in ``spacy.tokens.Doc`` object. The ``NP`` values are stored in ``doc._.noun_phrases``,

  Attributes:
    ext_name (str): customized extension field name
  """

  def __init__(self, nlp: Language):
    """Initialize the pipeline component. The shared nlp instance is used to initialize the matcher.
    
    Args:
      nlp (spacy.Language): language environment
    """
    lang = nlp.meta["lang"]
    self.ext_name = "noun_phrases"
    self.rule_module_name = 'phrase_detective.{}.noun_phrases'.format(lang)
    self.nlp = nlp

    if not Doc.has_extension(self.ext_name):
      Doc.set_extension(self.ext_name, default=[])

  def __call__(self, doc: Doc):
    """Apply the pipeline component on a ``Doc`` object and modify it if matches are found.

    Returns:
      Doc: with customized extension ``doc._.noun_phrases``
    """

    rule_module = import_module(self.rule_module_name) 
    fn = getattr(rule_module, 'search_out')
    doc._.noun_phrases = fn(doc, self.nlp) 
    return doc

