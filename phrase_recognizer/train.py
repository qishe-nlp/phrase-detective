import spacy
from phrase_recognizer import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer
import click
import json
import csv

def write_to_csv(fields, content, csvfile="review.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, encoding="utf8", mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)


@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--senfile", help="Specify the sentence file", prompt="Sentence file")
@click.option("--dstfile", help="Specify the noun phrase review file", prompt="Review file")
def generate_np_review_set(lang, senfile, dstfile):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = NounPhraseRecognizer(nlp)
  nlp.add_pipe(recognizer)

  with open(senfile, encoding="utf8") as f:
    TEXTS = json.loads(f.read())

  content = []
  for doc in nlp.pipe(TEXTS):
    nps = [np.text for np in doc._.noun_phrases]
    content.append({"sentence": doc.text, "nps": nps})

  write_to_csv(["sentence", "nps"], content, csvfile=dstfile)



@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--senfile", help="Specify the sentence file", prompt="Sentence file")
@click.option("--dstfile", help="Specify the noun phrase review file", prompt="Review file")
def generate_pp_review_set(lang, senfile, dstfile):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = PrepPhraseRecognizer(nlp)
  nlp.add_pipe(recognizer)

  with open(senfile, encoding="utf8") as f:
    TEXTS = json.loads(f.read())

  content = []
  for doc in nlp.pipe(TEXTS):
    pps = [np.text for np in doc._.prep_phrases]
    content.append({"sentence": doc.text, "pps": pps})

  write_to_csv(["sentence", "pps"], content, csvfile=dstfile)



@click.command()
@click.option("--lang", help="Specify the language", default="en", prompt="Language")
@click.option("--senfile", help="Specify the sentence file", prompt="Sentence file")
@click.option("--dstfile", help="Specify the noun phrase review file", prompt="Review file")
def generate_vkb_review_set(lang, senfile, dstfile):
  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  nlp = spacy.load(pkgindices[lang])

  recognizer = VerbKnowledgeRecognizer(nlp)
  nlp.add_pipe(recognizer)

  with open(senfile, encoding="utf8") as f:
    TEXTS = json.loads(f.read())

  content = []
  for doc in nlp.pipe(TEXTS):

    vs = ["TEXT: {}, VARIATION: {}, ORIGNAL: {}".format(v.text, v.tag_, v.lemma_) for v in doc._.verbs]
    pps = [pp.text for pp in doc._.passive_phrases]
    vps = [vp for vp in doc._.verb_phrases]
    
    content.append({"sentence": doc.text, "vs": vs, "pps": pps, "vps": vps})

  write_to_csv(["sentence", "vs", "pps", "vps"], content, csvfile=dstfile)




