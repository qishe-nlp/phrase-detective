from spacy.matcher import Matcher
from spacy.tokens import Doc, Span, Token
from phrase_recognizer.constants import VERB_PATTERNS, PASSIVE_PATTERNS
from phrase_recognizer.lib import merge

class VerbKnowledgeRecognizer(object):
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

    self.nlp = nlp
    self.matcher = Matcher(nlp.vocab)

    # TODO: 
    lang = nlp.meta["lang"]
    verb_patterns = VERB_PATTERNS[lang]
    passive_phrase_patterns = PASSIVE_PATTERNS[lang]


    self.matcher.add("VERB", None, *verb_patterns)
    self.matcher.add("PASSIVE", None, *passive_phrase_patterns)

    Doc.set_extension("verbs", default=[])
    Doc.set_extension("passive_phrases", default=[])
    Doc.set_extension("verb_phrases", default=[])

    self._reset_matchstore()

  def _reset_matchstore(self):
    self.match_store = {
      "VERB": [],
      "PASSIVE": [],
    }

   
  def __call__(self, doc):
    """
    Apply the pipeline component on a Doc object and modify it if matches are found.
    Return the Doc, so it can be processed by the next component in the pipeline, if available.
    """
    matches = self.matcher(doc)

    for match_id, start, end in matches:
      match_name = self.nlp.vocab.strings[match_id]
      self.match_store[match_name].append((start, end))

    self.get_verbs(doc, self.match_store["VERB"])
    self.get_passive_phrases(doc, self.match_store["PASSIVE"])
    self.get_verb_phrases(doc)

    self._reset_matchstore()

    return doc

  def get_verbs(self, doc, matches):
    verbs = []
    refined_matches = merge(matches)
    for start, _ in refined_matches:
      v = doc[start]
      verbs.append(v)
    doc._.verbs = verbs 

  def get_passive_phrases(self, doc, matches):
    passive_phrases = []
    refined_matches = merge(matches)
    for start, end in refined_matches:
      p = Span(doc, start, end)
      passive_phrases.append(p)
    doc._.passive_phrases = passive_phrases 

  def _get_en_verb_phrases(self, doc):
    verb_phrases = []
    for v in doc._.verbs:
      vp = {"verb": v.lemma_} 
      for obj in v.children:
        if obj.dep_ == "dobj":
          vp["direct object"] = " ".join([t.text for t in obj.subtree])
        if obj.dep_ == "dative":
          vp["indirect object"] = " ".join([t.text for t in obj.subtree])
      if "direct object" in vp.keys() or "indirect object" in vp.keys():
        verb_phrases.append(vp)

    doc._.verb_phrases = verb_phrases

  def _get_es_verb_phrases(self, doc):
    verb_phrases = []
    for v in doc._.verbs:
      vp = {"lemma": v.lemma_, "complete verb": v.text, "direct object": [], "indirect object": []} 
      for obj in v.children:
        if obj.i == v.i - 1 and obj.dep_ == "aux" and v.text != v.lemma_ :
          vp["complete verb"] = " ".join([t.text for t in obj.subtree]) + " " + v.text 
        if obj.dep_ == "obj":
          vp["direct object"].append(" ".join([t.text for t in obj.subtree]))
        if obj.dep_ == "iobj":
          vp["indirect object"].append(" ".join([t.text for t in obj.subtree]))
      if len(vp["direct object"]) > 0 or len(vp["indirect object"]) > 0:
        verb_phrases.append(vp)

    doc._.verb_phrases = verb_phrases
 
  def get_verb_phrases(self, doc):
    lang = self.nlp.meta["lang"]
    if lang == "en":
      self._get_en_verb_phrases(doc)
    elif lang == "es":
      self._get_es_verb_phrases(doc)

         

