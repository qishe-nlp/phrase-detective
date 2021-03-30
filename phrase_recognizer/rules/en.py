def get_verb_phrases(doc):
  """Get ``English`` verb phrases according to dependency parsing tags and verb detection

  Args:
    doc (spacy.tokens.Doc): sentence with meta information

  Returns:
    list: verb phrases with grammar description
  """

  verb_phrases = []
  for v in doc._.verbs:
    vp = {"lemma": v.lemma_, "complete verb": v.text, "direct object": [], "indirect object": []} 
    for obj in v.children:
      if obj.i == v.i - 1 and obj.dep_ == "aux" and v.text != v.lemma_ :
        vp["complete verb"] = " ".join([t.text for t in obj.subtree]) + " " + v.text 
      if obj.dep_ == "dobj":
        vp["direct object"].append(" ".join([t.text for t in obj.subtree]))
      if obj.dep_ == "dative":
        vp["indirect object"].append(" ".join([t.text for t in obj.subtree]))
    if len(vp["direct object"]) > 0 or len(vp["indirect object"]) > 0:
      verb_phrases.append(vp)
  return verb_phrases


en_rules = {
  "vp": get_verb_phrases,
}
