def passwort():
    passwort = str(input("Bitte geben Sie den Passwort ein: "))
    while True:
        passwort = str(input("Bitte geben Sie den Passwort ein: "))
        if passwort == "Italia":
            print("zugang gewährt")
            break
        else:
            print("falsches Passwort! versuch es nochmal")
passwort()
