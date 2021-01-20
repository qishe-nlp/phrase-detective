from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from phrase_recognizer.constants import PP_PATTERNS
from phrase_recognizer.lib import merge

class PrepPhraseRecognizer(object):
  """
  Customerized component to detect noun phrases in doc.
  The values are stored in doc._.prep_phrases 
  """

  name = "prep_phrases"

  def __init__(self, nlp):
    """
    Initialize the pipeline component. The shared nlp instance is used to
    initialize the matcher, which detects POS, TAG, DEP
    """

    self.matcher = Matcher(nlp.vocab)
    patterns = PP_PATTERNS[nlp.meta["lang"]]
    self.matcher.add("PP", None, *patterns)

    Doc.set_extension("prep_phrases", default=[])
    

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
      if doc[start].text not in ['of', 'to', 'a']: # TODO: It is bad
        np = Span(doc, start, end)
        phrases.append(np)
    doc._.prep_phrases = phrases
    return doc
