import random
def ratespiel():
    print("Willkommen beim Ratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht. Rate mal: ")
    zufallszahl = random.randint(1,10)
    
    while True:
        try:
            eingabe = int(input("Dein Tipp: "))
            if eingabe == zufallszahl:
                print("Richtig geraten!")
                break
            else:
                print("Leider falsch. Versuche es noch einmal.")
        except ValueError:
            print("Bitte gib eine ganze Zahl zwischen 1 und 10 ein.")

ratespiel()