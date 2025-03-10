def gerade_und_ungerade_Zahlen():
    print("Programm zur Unterscheidung von geraden und ungeraden Zahlen")

    while True:
        try:
            zahl = float(input("Bitte geben Sie eine Zahl ein: "))
            if zahl % 2 == 0:
                print("Die Zahl", zahl, "ist gerade.")
            else:
                print("Die Zahl", zahl, "ist ungerade.")
        except ValueError:
            print("Bitte geben Sie eine ganze Zahl ein.")
        wahl = input("Möchten Sie eine weitere Zahl eingeben? ja/nein ").lower()
        if wahl == "nein":
            print("Auf Wiedersehen!")
            break
        elif wahl == "ja":
            continue
        else:
            print("Ungültige Eingabe.")
            break

gerade_und_ungerade_Zahlen()
