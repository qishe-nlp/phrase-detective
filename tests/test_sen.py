from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    "This isn’t anything important.",
    "He wanted to get someone reliable to help in this work.",
    "People here know each other.",
    "It had been fine the day before.",

    "He is a student of astronomy.",
    "Even a small rise in interest rates would hurt borrowers.",

    "He looked at me from behind the tree.",
    "I can't see you until after lunch.",

    "Just come through here and I ’ll show you where the problem is.",
    "Many of these treatments were used until quite recently.",

    "They left just after six о'clock.",
    "There will be a concert on New Year's Day.",
    "Typhoons seldom come in winter.",
    "The short video spread quickly in China.",
  ]

  sens = [
    #"Los tres chicos son de mi barrio.",
    "Me gusta tu caminar.",
    #"La desesperada se marchó sola.",
    #"Ella es mi compañera de clase.",
    #"Me gusta la biblioteca de mi universidad."
    #"Un hombre salió de entre la gente.",
    #"Perdió la guerra por ambicioso.",
    "El Gobierno aún tiene por delante una difícil tarea.",
  ]

  sens = [
    "A surfboard is made out of a core element",
    "he was mesmerized by hundreds of people in the water,",
    "between surfer and shaper.",
  ]

  sens = [
    #"Lo que tengo ganas es de que podamos salir a la calle.",
    #"Es que en el ordenador las ponemos a cámara rápida, se llama Timelapse.",
    #"Qué día más chungo hace, no papá?",
    #"Pero lo más rollo es hacer las fichas por la trade.",
    "Más tragedias encima ahora mismo?",
    "No es lo mío.",
    "Porqué no haces un timelapse de esos para que todo esto pase rápido?",
  ]

  #sens = []
  lang = "es"
  nlp = spacy.load(PKG_INDICES[lang])
  for sentence in sens:
    doc = nlp(sentence)
    for t in doc:
      print("{}: {} {} {} {}".format(t.text, t.pos_, t.morph, t.tag_, t.dep_))
    print()

