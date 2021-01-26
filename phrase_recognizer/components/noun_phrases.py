from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from phrase_recognizer.constants import NP_PATTERNS
from phrase_recognizer.lib import merge

class NounPhraseRecognizer(object):
  """
  Customerized component to detect noun phrases in doc.
  The values are stored in doc._.noun_phrases 
  """

  name = "noun_phrases"

  def __init__(self, nlp):
    """
    Initialize the pipeline component. The shared nlp instance is used to
    initialize the matcher, which detects POS
    """

    self.matcher = Matcher(nlp.vocab)
    patterns = NP_PATTERNS[nlp.meta["lang"]]
    self.matcher.add("NP", None, *patterns)

    Doc.set_extension("noun_phrases", default=[])
    

  def __call__(self, doc):
    """
    Apply the pipeline component on a Doc object and modify it if matches are found.
    Return the Doc, so it can be processed by the next component in the pipeline, if available.
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
    Doc.remove_extension("noun_phrases")
