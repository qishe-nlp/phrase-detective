# -*- coding: utf-8 -*-
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span, Token
from phrase_detective.lib import merge
from phrase_detective.regx import REGX
from phrase_detective.rules import RULES

class VerbKnowledgeRecognizer:
  """Customerized component to detect verb knowledge in ``spacy.tokens.Doc`` object. The corresponding values are stored in ``doc._.verbs``, ``doc._.passive_phrases``, and ``doc._.verb_phrases``.

  Attributes:
    ext_name (str): customized extension field name
    matcher (spacy.mathcer.Matcher): Rule maker for detecting ``VERB`` and ``PASSIVE``
  """

  def __init__(self, nlp):
    """Initialize the pipeline component. The shared nlp instance is used to initialize the matcher.
    
    Args:
      nlp (spacy.Language): language environment
    """

    self.nlp = nlp
    self.matcher = Matcher(nlp.vocab)

    lang = nlp.meta["lang"]
    patterns = REGX[lang] 
    verb_patterns = patterns["verb"]
    passive_phrase_patterns = patterns["verb_passive"]
    self.rules = RULES[lang]

    self.matcher.add("VERB", verb_patterns)
    self.matcher.add("PASSIVE", passive_phrase_patterns)

    if not Doc.has_extension("verbs"):
      Doc.set_extension("verbs", default=[])
    if not Doc.has_extension("passive_phrases"):
      Doc.set_extension("passive_phrases", default=[])
    if not Doc.has_extension("verb_phrases"):
      Doc.set_extension("verb_phrases", default=[])

    self._reset_matchstore()

  def _reset_matchstore(self):
    self.match_store = {
      "VERB": [],
      "PASSIVE": [],
    }
   
  def __del__(self):
    """Remove customized extensions ``doc._.verb_phrases``, ``doc._.verbs`` and ``doc._.passive_phrases``
    """
    if Doc.has_extension("verbs"):
      Doc.remove_extension("verbs")
    if Doc.has_extension("passive_phrases"):
      Doc.remove_extension("passive_phrases")
    if Doc.has_extension("verb_phrases"):
      Doc.remove_extension("verb_phrases")


  def __call__(self, doc):
    """Apply the pipeline component on a Doc object and modify it if matches are found.

    Returns:
      Doc: with customized extensions ``doc._.verb_phrases``, ``doc._.passive_phrases``, `doc._.verbs` 
    """
    matches = self.matcher(doc)

    for match_id, start, end in matches:
      match_name = self.nlp.vocab.strings[match_id]
      self.match_store[match_name].append((start, end))

    self._get_verbs(doc, self.match_store["VERB"])
    self._get_passive_phrases(doc, self.match_store["PASSIVE"])
    self._get_verb_phrases(doc)

    self._reset_matchstore()

    return doc

  def _get_verbs(self, doc, matches):
    verbs = []
    refined_matches = merge(matches)
    for start, _ in refined_matches:
      v = doc[start]
      verbs.append(v)
    doc._.verbs = verbs 

  def _get_passive_phrases(self, doc, matches):
    passive_phrases = []
    refined_matches = merge(matches)
    for start, end in refined_matches:
      p = Span(doc, start, end)
      passive_phrases.append(p)
    doc._.passive_phrases = passive_phrases 

  def _get_verb_phrases(self, doc):
    doc._.verb_phrases = self.rules["vp"](doc)

