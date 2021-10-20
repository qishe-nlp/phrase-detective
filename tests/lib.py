from spacy.language import Language
from phrase_detective import NounPhraseRecognizer, VerbKnowledgeRecognizer
from spacy import displacy
from pathlib import Path
import json
import csv
import spacy

@Language.factory("nprecog")
def create_np_parser(nlp: Language, name: str):
  return NounPhraseRecognizer(nlp) 

@Language.factory("vkbrecog")
def create_vkb_parser(nlp: Language, name: str):
  return VerbKnowledgeRecognizer(nlp) 

def print_doc(doc):
  for t in doc:
    print("{} {} {} {} {}".format(t.text, t.tag_, t.pos_, t.dep_, t.lemma_))


def graph(doc, lang):
  svg = displacy.render(doc, style="dep", jupyter=False)
  file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
  output_path = Path(lang+ "_images/" + file_name)
  output_path.open("w", encoding="utf-8").write(svg)

def show_np(nlp, sentences):
  for s in sentences:
    doc = nlp(s)
    nps = []
    print(s)
    graph(doc, nlp.meta["lang"])
    #print_doc(doc)
    for np in doc._.noun_phrases:
      nps.append(np.text)
    print(nps)

def show_vkb(nlp, sentences):
  for s in sentences:
    doc = nlp(s)
    nps = []
    print(s)
    graph(doc, nlp.meta["lang"])
    for v in doc._.verbs:
      print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))


def _write_to_csv(fields, content, csvfile="review.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, encoding="utf8", mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)


def write2csv(sentences, nlp, rules):
  content = {}
  for r in rules:
    content[r] = []

  for s in sentences:
    doc = nlp(s)
    for r in rules:
      info = {
        "sentence": doc.text,
        r: json.dumps([t.text for t in doc._.noun_phrases])
      }
      content[r].append(info)
  # write to multiple files
  for k, v in content.items():
    _write_to_csv(["sentence", k], v, csvfile="tbr/"+k+".csv")
    


