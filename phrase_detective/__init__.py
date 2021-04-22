# -*- coding: utf-8 -*-
"""``phrase_detective`` Package

Components for ``spacy`` pipeline, to detect noun phrase, prep phrase, verb related knowledge

.. topic:: Install package

  .. code:: shell
    
    $ pip3 install --index-url https://test.pypi.org/simple/ \\
      --extra-index-url https://pypi.org/simple \\
      --verbose phrase_detective

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

.. topic:: Example: Detect preposition phrases 

  .. code:: python 

    import spacy
    from spacy import Language
    from phrase_detective import PrepPhraseRecognizer, PKG_INDICES

    @Language.factory("pprecog")
    def create_pp_parser(nlp: Language, name: str):
      return PrepPhraseRecognizer(nlp) 

    def prep_phrase(lang, sentence):
      nlp = spacy.load(PKG_INDICES[lang])
      nlp.add_pipe("pprecog")
      doc = nlp(sentence)
      for np in doc._.prep_phrases:
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
      for pp in doc._.passive_phrases:
        print(pp.text)
      for vp in doc._.verb_phrases:
        print(vp)

"""

__version__ = '0.1.9'

from .components import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer
from .constants import PKG_INDICES
