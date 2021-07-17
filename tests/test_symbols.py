from spacy.language import Language
from phrase_detective import PKG_INDICES
import spacy

def test_de():
  TAG = ["$(", "$,", "$.", "ADJA", "ADJD", "ADV", "APPO", "APPR", "APPRART", "APZR", "ART", "CARD", "FM", "ITJ", "KOKOM", "KON", "KOUI", "KOUS", "NE", "NN", "NNE", "PDAT", "PDS", "PIAT", "PIS", "PPER", "PPOSAT", "PPOSS", "PRELAT", "PRELS", "PRF", "PROAV", "PTKA", "PTKANT", "PTKNEG", "PTKVZ", "PTKZU", "PWAT", "PWAV", "PWS", "TRUNC", "VAFIN", "VAIMP", "VAINF", "VAPP", "VMFIN", "VMINF", "VMPP", "VVFIN", "VVIMP", "VVINF", "VVIZU", "VVPP", "XY"]
  for t in TAG:
    e = spacy.explain(t)
    print("{} {}".format(t, e))

  DEP = ["ROOT", "ac", "adc", "ag", "ams", "app", "avc", "cc", "cd", "cj", "cm", "cp", "cvc", "da", "dep", "dm", "ep", "ju", "mnr", "mo", "ng", "nk", "nmc", "oa", "oc", "og", "op", "par", "pd", "pg", "ph", "pm", "pnc", "punct", "rc", "re", "rs", "sb", "sbp", "svp", "uc", "vo"]
  for d in DEP:
    e = spacy.explain(d)
    print("{} {}".format(d, e))

def test_en():
  TAG = ["$", "''", ",", "-LRB-", "-RRB-", ".", ":", "ADD", "AFX", "CC", "CD", "DT", "EX", "FW", "HYPH", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NFP", "NN", "NNP", "NNPS", "NNS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB", "XX", "``"]

  for t in TAG:
    e = spacy.explain(t)
    print("{} {}".format(t, e))

  DEP = ["ROOT", "acl", "acomp", "advcl", "advmod", "agent", "amod", "appos", "attr", "aux", "auxpass", "case", "cc", "ccomp", "compound", "conj", "csubj", "csubjpass", "dative", "dep", "det", "dobj", "expl", "intj", "mark", "meta", "neg", "nmod", "npadvmod", "nsubj", "nsubjpass", "nummod", "oprd", "parataxis", "pcomp", "pobj", "poss", "preconj", "predet", "prep", "prt", "punct", "quantmod", "relcl", "xcomp"]
  for d in DEP:
    e = spacy.explain(d)
    print("{} {}".format(d, e))


def test_es():

  DEP = ["ROOT", "acl", "advcl", "advmod", "amod", "appos", "aux", "case", "cc", "ccomp", "compound", "conj", "cop", "csubj", "dep", "det", "expl:pass", "fixed", "flat", "iobj", "mark", "nmod", "nsubj", "nummod", "obj", "obl", "parataxis", "punct", "xcomp"]
  for d in DEP:
    e = spacy.explain(d)
    print("{} {}".format(d, e))

