from phrase_detective import PKG_INDICES
import spacy
from tests.lib import *


lang = "es"
nlp = spacy.load(PKG_INDICES[lang])
nlp.add_pipe("nprecog")
nlp.add_pipe("vkbrecog")

sentences = [
  "A Pablo le gustaban las niñas pijas como a ti.",
]


def test_es_nprecog():
  show_np(nlp, sentences)
 

def test_es_vkbrecog():
  show_vkb(nlp, sentences)
