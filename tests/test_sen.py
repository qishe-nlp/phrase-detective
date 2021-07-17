from phrase_detective import PKG_INDICES
import spacy

def test_sens():
  sens = [
    "Sie können Markus Klepper auch gerne anrufen, wenn Sie ganz konkrete Fragen haben.",
    "Erst als ihn Soldaten stützen und ihm frisches Wasser bringen, dämmert es ihm, dass er gerettet ist.",
    "Ihre Lieferanten sind pures Gold , man muss es nur aus der Erde holen.",
    "Ältere Kinder , Jugendliche oder Erwachsene werden bei ihrer Taufe gefragt.",
    "Sie begannen, in fremden Sprachen zu reden, wie es der Geist ihnen eingab",
    "Für die angesprochene 'innerislamische Diskussion' brauchen wir auch öffentliche Plattformen und keine dumpfen Machtdemonstrationen des Staates."
  ]


  sens = [
    "Mai ist für alle Menschen der Tag des Widerstands gegen Ausbeutung und Unterdrückung.",
    "1938 wurde das Haus des Gastwirts Pommer von Martin Bormann für die NSDAP gekauft.",
    "So hat doch dieses heute Morgen in euch das Licht entfacht, das Licht der Sonne, das Licht der Liebe und das Licht welches in euch ist und hierdurch nun verstärkt wird.",
    "Nach der Wesensverwandlung bekommen die Gestalten des Brotes und Weines ohne Zweifel eine neue Bedeutung und einen neuen Zweck.",
    "Als eigenständige Religionsgemeinschaft hat die Alevitengemeinde die Auswahl der Lehrkräfte vorgenommen.",
    "Manche Erinnerungen sind bei uns verschüttet mal weil sie nicht wichtig waren, mal weil sie uns erschreckten oder die Reaktion der Erwachsenen auf unsere Aussagen.",
  ]
  
  sens = [
    "Die RKW hat der Bischof selbst als Junge in seiner damaligen Heimat kennen gelernt.",
    "Unser Cloudspeicher löst dieses Problem elegant durch normierte Zugangswege, höchste Verfügbarkeit und dem Vertrauen die Daten dort zu speichern.",
    "Was das Internet derzeit noch nicht kann: Unterricht erteilen und dabei auf die Fragen antworten.",
    "Sie können sich freiwillig an den Unkosten jeweils Ende Jahr mit beigelegtem Einzahlungsschein beteiligen." 
  ]

  sens = [
    "Eine Vielzahl an Gebäuden wurde schwer beschädigt und die Bevölkerung ging bis auf die Hälfte zurück.",
    "Dabei handelt es sich um Sendungen bis zu einem Gewicht von drei Kilogramm.",
    "Die Schnur reicht bis ins Zimmer hinein.",
    "Problematisch hierbei ist insbesondere, dass die Gewerbesteuer ausschließlich bei Privatpersonen bis zu einem Hebesatz von 380 Prozent bei der Einkommenssteuer angerechnet werden kann.",
    "Zum Mitspielen und Anleiten sind eine Erzieherin und eine Helferin mit in der Gruppe.",
    "Der Arbeitsausschuss kann über Zuwendungen im Sinne des § 2 der Satzung bis zu einem Betrag von Euro 10.000,00 selbstständig entscheiden."
  ]

  sens = []
  lang = "de"
  nlp = spacy.load(PKG_INDICES[lang])
  for sentence in sens:
    doc = nlp(sentence)
    for t in doc:
      print("{}: {} {} {} {}".format(t.text, t.pos_, t.morph, t.tag_, t.dep_))
    print()

