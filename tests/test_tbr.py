import spacy
from phrase_detective import PKG_INDICES
from tests.lib import *
import json

lang = "de"
pkg = PKG_INDICES[lang]

# read srt to json obj file
tbr_sentences = [
]

def read_json(filename):
  data = []
  with open(filename) as f:
    data = json.load(f)
  return data


def test_np():
  sentences = tbr_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('nprecog')
  ext_name = nlp.get_pipe("nprecog").ext_name
  write2csv(sentences, nlp, [ext_name])


def test_tbr_gen():
  sentences = read_json('./de_S01E06.json')
  #sentences = tbr_sentences 

  print(sentences)
  nlp = spacy.load(pkg)
  nlp.add_pipe('nprecog')
  ext_name = nlp.get_pipe("nprecog").ext_name
  write2csv(sentences, nlp, [ext_name])

