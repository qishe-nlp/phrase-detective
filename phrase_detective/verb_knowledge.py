# -*- coding: utf-8 -*-
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span, Token
from spacy.language import Language 
from phrase_detective.regx import REGX 

class VerbKnowledgeRecognizer:
  """Customerized component to detect verb knowledge in ``spacy.tokens.Doc`` object. The corresponding values are stored in ``doc._.verbs``.

  Attributes:
    ext_name (str): customized extension field name
    matcher (spacy.mathcer.Matcher): Rule maker for detecting ``VERB``
  """

  def __init__(self, nlp: Language):
    """Initialize the pipeline component. The shared nlp instance is used to initialize the matcher.
    
    Args:
      nlp (spacy.Language): language environment
    """

    self.nlp = nlp
    self.matcher = Matcher(nlp.vocab)
    self.ext_name = "verbs"

    lang = nlp.meta["lang"]
    verb_patterns = REGX[lang] 

    self.matcher.add("VERB", verb_patterns)

    if not Doc.has_extension(self.ext_name):
      Doc.set_extension(self.ext_name, default=[])

  def __call__(self, doc):
    """Apply the pipeline component on a Doc object and modify it if matches are found.

    Returns:
      Doc: with customized extensions `doc._.verbs` 
    """
    matches = self.matcher(doc)

    verbs = []
    ids = list(dict.fromkeys([start for _, start, end in matches if end-start==1]))
    for e in ids:
      v = doc[e]
      verbs.append(v)
    doc._.verbs = verbs 

    return doc
