# -*- coding: utf-8 -*-
"""``phrase_detective`` Package

Components for ``spacy`` pipeline, to detect noun phrase, prep phrase, verb related knowledge

.. topic:: Install package

  .. code:: shell
    
    $ pip3 install --verbose phrase_detective
    $ python -m spacy download en_core_web_trf
    $ python -m spacy download es_dep_news_trf
    $ python -m spacy download de_dep_news_trf

.. topic:: Example: Detect noun phrases 

  .. code:: python

    import spacy
    from spacy import Language
    from phrase_detective import NounPhraseRecognizer, PKG_INDICES

    @Language.factory("nprecog")
    def create_np_parser(nlp: Language, name: str):
      return NounPhraseRecognizer(nlp) 

    def noun_phrase(lang, sentence):
      nlp = spacy.load(PKG_INDICES[lang])
      nlp.add_pipe("nprecog")
      doc = nlp(sentence)
      for np in doc._.noun_phrases:
        print(np.text)

.. topic:: Example: Detect verb phrases 

  .. code:: python

    import spacy
    from spacy import Language
    from phrase_detective import VerbKnowledgeRecognizer, PKG_INDICES

    @Language.factory("vkbrecog")
    def create_vkb_parser(nlp: Language, name: str):
      return VerbKnowledgeRecognizer(nlp) 

    def verb_knowledge(lang, sentence):
      nlp = spacy.load(PKG_INDICES[lang])
      nlp.add_pipe("vkbrecog")
      doc = nlp(sentence)
      for v in doc._.verbs:
        print("TEXT: {}, TAG: {}, FORM: {}, ORIGNAL: {}".format(v.text, v.tag_, spacy.explain(v.tag_), v.lemma_))

"""

__version__ = '0.1.31'

from .noun_phrases import NounPhraseRecognizer
from .verb_knowledge import VerbKnowledgeRecognizer
from .constants import PKG_INDICES
