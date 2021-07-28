from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    "So many of our brothers and sisters",
    "and our sons and brothers, husbands and fathers",
    "How could you contemplate such ruin and disappointment to yourself",
    "Over the coming weeks and months, you will all bear witness",
  ]

  sens = [
    "have given their lives in resistance to that occupation,",
    "An Olympian who's spent much of the past year on her backside.",
    "Salmon fishing with friends.",
    "They that go down to the sea in ships…",
  ]


  sens = [
    #"to conceal your infatuation for another man's wife.",
    #"I'm sure all the kids' dads love her too.",
    #"We've received a copy of a telegram",
    "She believes the people of Britain will help to accomplish it.",
    "I will not be drawn on any subject save the weather.",
  ]
  #sens = []
  lang = "en"
  nlp = spacy.load(PKG_INDICES[lang])
  docs = []
  for sentence in sens:
    doc = nlp(sentence)
    for t in doc:
      print("{}: {} {} {} {}".format(t.text, t.pos_, t.morph, t.tag_, t.dep_))
    print()
    docs.append(doc)
  #spacy.displacy.serve(docs, style="dep")

