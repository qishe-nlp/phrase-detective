from phrase_detective import PKG_INDICES
import spacy
from tests.lib import *

lang = "de"
nlp = spacy.load(PKG_INDICES[lang])
nlp.add_pipe("nprecog")
nlp.add_pipe("vkbrecog")


sentences = [
  "Unser Institut wird als Erstes wirksame Heilmittel",
  "Da ist meiner Detektiv seiner Zeit voraus.",
  "Und noch diese Frau Tuberkulin behandelt worden ist",
  "Das gleichen soll sie es nicht bemerken, wenn sie von einem Herren auffälligerweise",
  "Laufen Sie rüber zum Stall und mehr Glück.",
  "Alle haben Fieber und Schüttelfrost, und diese Reaktion belegt die Wirksamkeit.",
  "Bei der Aufnahme in unsere Gemeinschaft da,",
]

def test_de_nprecog():
  show_np(nlp, sentences)
 

def test_de_vkbrecog():
  show_vkb(nlp, sentences)
