def Taschenrechner ():

    zahl1 = float (input("bitte geben sie die erste zahl ein: "))
    operator = input("Wähle eine Operation (+, -, *, /): ")
    zahl2 = float (input("bitte geben sie die zweite zahl ein: "))
   
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        if zahl2 == 0:
            print("durch null teilen ist nicht erlaubt")
            return
        ergebnis = zahl1 / zahl2
    elif operator == "**":
        ergebnis = zahl1 ** zahl2
    else:
        print("ungültiger operator")
        return

    print("ergebnis:", ergebnis)

    wahl = input("Möchtest du zum Anfang zurückkehren? (ja/nein): ").lower()

    if wahl == "ja":
        Taschenrechner()  
    else:
        print("Auf Wiedersehen!")

Taschenrechner()


