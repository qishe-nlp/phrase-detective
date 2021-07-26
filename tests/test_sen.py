from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    #"I think the reason buttons have endured for so long, historically,",
    #"The one that we all think of is the pocket compass.",
    #"and come up with the compass rose.",
    #"Double Dutch jump rope remains a powerful symbol of culture and identity",
    #"which is why, I think, so many hiphop artists",
    "where this kind of roiling ball of molten iron",
    #"what north, south, east and west looked like,",
    "you get a lot more detail",
    "Magnetism is still a pretty mysterious force to physicists,",
    "you are in touch with the very center of our planet,",
    "where this kind of roiling ball of molten iron",
    #"but you can also reliably find your way home.",
  ]
  sens = [
    "die jetzt alle oben verbreitet werden, auch von den Ärzten der Charité.",
    "Sollte sie jedoch die nächsten 24 Stunden überstehen und das Fieber sinken, hat sie eine Chance.",
    "und der Gesetzentwurf zur Beschränkung der Kinderarbeit liegen bereits in meiner Schublade.",
    "Unruhe ist ein Zeichen von Schmerzen. Tischendorf.",
    "Er wird ein aufgehender Stern am Forscherhimmel des Koch'schen Instituts."
    "Atemgeräusche über der Lungenspitze sind deutlich abgeschwächt.",
    "Deren medizinische Vorstellungen in der Journal sind teilweise abenteuerlich.",
    "Meine Herren, vergessen Sie nie, den Segen, den das Chloroform in die Operationssäle gebracht hat.",
  ]

  sens = [
    #"qué tal doña concha?",
    #"Ten cuidado bonito! No te vayas a tropezar y te rompes los dientes contra un banco",
    #"Pues es que a mí me duele la espalda y la vértebra y tengo un disco rayado",
    "Encima voy a ser yo el malo de la película!",
    "Y ahora noto como...como como un poco de angustia y me cuesta respirar pero es de ilusión",
    "O mejor, se lo voy a decir a mi madre que venga un par de veces por semana",
    "Deja en paz a la gente que te pones muy pesada",
  ]
  #sens = []
  lang = "es"
  nlp = spacy.load(PKG_INDICES[lang])
  docs = []
  for sentence in sens:
    doc = nlp(sentence)
    for t in doc:
      print("{}: {} {} {} {}".format(t.text, t.pos_, t.morph, t.tag_, t.dep_))
    print()
    docs.append(doc)
  #spacy.displacy.serve(docs, style="dep")

