def Zahlenraten():
   import random
   zufallszahlen =random.randint(1,10)
   versuche = 5
   print("willkommen beim Zahlenraten")
   print("ich habe mir eine Zahl zwischen 1 und 10 ausgedacht")
   print("rate mal")

   while versuche > 0:
    try:
      zahl = int(input("Dein Tipp: "))
      if zahl == zufallszahlen:
         print("Glückwunsch, du hast die Zahl erraten")
         return
      elif zahl < zufallszahlen:
         print("die gesuchte zahl ist größer")
      else:
         print("die gesuchte zahl ist kleiner")
         versuche -= 1 
    except ValueError:
         print("das war keine Zahl")
         print("du hast noch", versuche, "versuche")
         print("leider hast du verloren")
         print("die gesuchte zahl war:", zufallszahlen)

Zahlenraten()

        
   