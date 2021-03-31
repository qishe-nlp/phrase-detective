# Installation from pip3

```shell
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose phrase_recognizer 
python -m spacy download en_core_web_trf
python -m spacy download es_dep_news_trf
```

# Usage

### Detect noun phrases 
```
import spacy
from spacy import Language
from phrase_recognizer import NounPhraseRecognizer, PKG_INDICES

@Language.factory("nprecog")
def create_np_parser(nlp: Language, name: str):
  return NounPhraseRecognizer(nlp) 

def noun_phrase(lang, sentence):
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("nprecog")
  doc = nlp(sentence)
  for np in doc._.noun_phrases:
    print(np.text)

```
### Detect preposition phrases 

```
import spacy
from spacy import Language
from phrase_recognizer import PrepPhraseRecognizer, PKG_INDICES

@Language.factory("pprecog")
def create_pp_parser(nlp: Language, name: str):
  return PrepPhraseRecognizer(nlp) 

def prep_phrase(lang, sentence):
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("pprecog")
  doc = nlp(sentence)
  for np in doc._.prep_phrases:
    print(np.text)
```

### Detect verb phrases 

```
import spacy
from spacy import Language
from phrase_recognizer import VerbKnowledgeRecognizer, PKG_INDICES

@Language.factory("vkbrecog")
def create_vkb_parser(nlp: Language, name: str):
  return VerbKnowledgeRecognizer(nlp) 

def verb_knowledge(lang, sentence):
  nlp = spacy.load(PKG_INDICES[lang])
  nlp.add_pipe("vkbrecog")
  doc = nlp(sentence)
  for v in doc._.verbs:
    print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))
  for pp in doc._.passive_phrases:
    print(pp.text)
  for vp in doc._.verb_phrases:
    print(vp)
```

# Development

### Clone project
```
git clone https://github.com/qishe-nlp/phrase-recognizer.git
```

### Install [poetry](https://python-poetry.org/docs/)

### Install dependencies
```
poetry update
```

### Test and Issue
```
poetry run pytest -rP
```
which run tests under `tests/*`

### Create sphix docs
```
poetry shell
cd apidocs
sphinx-apidoc -f -o source ../phrase_recognizer
make html
python -m http.server -d build/html
```

### Build
* Change `version` in `pyproject.toml` and `phrase_recognizer/__init__.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`

# TODO

### Github action to publish package
* pypi test repo
* pypi repo
