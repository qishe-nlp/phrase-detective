from phrase_detective import PKG_INDICES
import spacy
from tests.lib import *


lang = "en"
nlp = spacy.load(PKG_INDICES[lang])
nlp.add_pipe("nprecog")
nlp.add_pipe("vkbrecog")

sentences = [
  "It's a miraculous and distinctly human gift.",
  "You know, you have to stand up in front of somebody,",
  "Okay, you guys all know what emotions are, right?",
]


def test_en_nprecog():
  show_np(nlp, sentences)
 

def test_en_vkbrecog():
  show_vkb(nlp, sentences)
