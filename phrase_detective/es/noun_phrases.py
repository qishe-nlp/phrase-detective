from spacy.matcher import DependencyMatcher, Matcher
from phrase_detective.lib import merge

def search_out(doc, nlp):
  """Search for prepositions with verb 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """
  result = []

  token_matcher = Matcher(nlp.vocab)
  dep_matcher = DependencyMatcher(nlp.vocab)
  
  token_patterns = [
    [{"LOWER": {"IN": ["más", "mneos"]}}, {"POS": "NOUN"}, {"LOWER": "que"}, {}],
    [{"POS": "NOUN"}, {"POS": "PRON", "DEP": "compound"}],
    [{"POS": "DET", "DEP": {"IN": ["det", "amod"]}, "OP": "*"}, {"POS": "NUM", "DEP": "nummod", "OP": "?"}, {"POS": "ADJ", "DEP": "amod", "OP": "*"}, {"POS": "NOUN"}],
    [{"POS": "DET", "DEP": {"IN": ["det", "amod"]}, "OP": "*"}, {"POS": "ADV", "DEP": "advmod", "OP": "?"}, {"POS": "ADJ", "DEP": "amod", "OP": "+"}, {"POS": "NOUN"}],
  ]
  token_matcher.add("token_NP", token_patterns)
  token_matches = token_matcher(doc)

  token_refined_matches = merge([(start, end) for _, start, end in token_matches])


  dep_patterns = [
    [
      {
        "RIGHT_ID": "noun",
        "RIGHT_ATTRS": {"POS": "NOUN"}
      },
      {
        "LEFT_ID": "noun",
        "REL_OP": ">",
        "RIGHT_ID": "mod",
        "RIGHT_ATTRS": {"DEP": {"IN": ["nmod", "amod"]}}
      },
    ],
  ]

  dep_matcher.add("dep_NP", dep_patterns)
  dep_matches = dep_matcher(doc)
  dep_refined_matches = []
  for _, (noun, desp) in dep_matches:
    desp_tree = [e.i for e in doc[desp].subtree]
    length_valid = len(desp_tree) == max(desp_tree) - min(desp_tree) + 1
    noun_valid = any([noun<=end and noun>=start for start, end in token_refined_matches])
    if length_valid and noun_valid and noun < desp:
      desp_tree.append(noun)
      desp_tree.sort()
      dep_refined_matches.append((min(desp_tree),max(desp_tree)+1))
      
  matches = token_refined_matches + dep_refined_matches
  refined_matches = merge(matches)

  for start, end in refined_matches:
    if end-start > 1 and all([e.pos_!="PUNCT" for e in doc[start:end]]):
      np = doc[start: end]
      result.append(np)

  return result
   
