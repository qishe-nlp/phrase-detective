import spacy
from phrase_recognizer import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer
import click
import json
import csv
from spacy import displacy

@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--sentence", help="Specify the sentence", prompt="Sentence")
def analyze(lang, sentence):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  doc = nlp(sentence)
  for t in doc:
    print("text: {}, pos: {}, tag: {}, form: {}, lemma: {}, dep: {}, head: {}". format(t.text, t.pos_, t.tag_, spacy.explain(t.tag_), t.lemma_, t.dep_, t.head.text))
    left_tree = [e for e in t.lefts]
    right_tree = [e for e in t.rights]

    linfo = " ".join([e.text for e in left_tree[0].subtree]) if len(left_tree) > 0 else ""
    rinfo = " ".join([e.text for e in right_tree[0].subtree]) if len(right_tree) > 0 else ""

    print("text: {}, pos: {}, leftchild: {}, rightchild: {}". format(t.text, t.pos_, linfo, rinfo))


  displacy.serve(doc, style="dep")

@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--sentence", help="Specify the sentence", prompt="Sentence")
def noun_phrase(lang, sentence):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = NounPhraseRecognizer(nlp)
  nlp.add_pipe(recognizer)
  doc = nlp(sentence)
  #for t in doc:
  #  print("POS: {}, TAG: {}, TEXT: {}". format(t.pos_, t.tag_, t.text))
  for np in doc._.noun_phrases:
    print(np.text)


@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--sentence", help="Specify the sentence", prompt="Sentence")
def prep_phrase(lang, sentence):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = PrepPhraseRecognizer(nlp)
  nlp.add_pipe(recognizer)
  doc = nlp(sentence)
  for np in doc._.prep_phrases:
    print(np.text)


@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--sentence", help="Specify the sentence", prompt="Sentence")
def verb_knowledge(lang, sentence):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = VerbKnowledgeRecognizer(nlp)
  nlp.add_pipe(recognizer)
  doc = nlp(sentence)
  for v in doc._.verbs:
    print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))
  for pp in doc._.passive_phrases:
    print(pp.text)
  for vp in doc._.verb_phrases:
    print(vp)

