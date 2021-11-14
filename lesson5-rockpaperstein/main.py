# So hätte "Endgame" eigentlich enden sollen: Mit Schere, Stein und Papier.
# Die ersten zwei Zeilen bereiten das Spiel und die grafische Ausgabe vor.
# Sie sollten unverändert ganz am Anfang des Programms stehen bleiben.
from endgame import endgame
endgame = endgame()

# SCHRITT 1
# Das Programm besteht bisher nur aus zwei Zeilen. Führe es aus und
# sieh nach, was passiert.

# SCHRITT 2
# Du spielst IronMan. Entscheide dich für Stein, Schere oder Papier.
# Speichere deine Auswahl als String in der Variablen handIronman.
# Tipp: Achte auf die Groß-/Kleinschreibung!
# Tipp: Ändere deine Auswahl nicht mehr, wenn du die folgenden Schritte programmierst.

handIronman = endgame.makeChoice()

# SCHRITT 3
# Starte den epischen Kampf, indem du die Funktion "endgame.startBattle()" aufrufst.
# Gib der Funktion als Parameter deine Auswahl aus Schritt 2 mit - 
# also die Variable handIronman.
# Man kann Funktionen Parameter mitgeben, indem man sie in die Klammern der Funktion schreibt.
# Speichere das Ergebnis der Funktion in der Variable handThanos.

handThanos = endgame.startBattle(handIronman)

# SCHRITT 4
# Gib auf dem Bildschirm aus, welches Handzeichen Ironman und Thanos haben.

print ("Ironman hat " + handIronman + ", Thanos hat " + handThanos + ".")

# SCHRITT 5
# Schreibe die Bedingungen dafür auf, dass es ein "Unentschieden" gibt.
# Wenn die Bedingungen zutreffen, dann gib auf dem Bildschirm aus: 
# "Es ist unentschieden!"

if handThanos == "Stein":
  print ("Es ist unentschieden!")

# SCHRITT 6
# Schreibe die Bedingungen dafür auf, dass Ironman gewinnt.
# Wenn die Bedingungen zutreffen, dann gib auf dem Bildschirm aus: 
# "Ironman hat gewonnen!"

if handThanos == "Schere":
  print ("Ironman hat gewonnen!")

# SCHRITT 7
# Schreibe die Bedingungen dafür auf, dass Thanos gewinnt.
# Wenn die Bedingungen zutreffen, dann gib auf dem Bildschirm aus: 
# "Thanos hat gewonnen!"

if handThanos == "Papier":
  print ("Thanos hat gewonnen!")

# Schritt 8 
# Ab jetzt sollen Benutzer:innen erst beim Ausführen des Programms
# entscheiden, ob sie Schere, Stein oder Papier möchten.
# Dafür dient die Funktion "endgame.makeChoice()".
# Ändere deine Auswahl in Schritt 2 so, dass endgame.makeChoice() aufgerufen wird.
# Das Ergebnis soll weiterhin in der Variable handIronman gespeichert werden.

# Schritt 9
# Frage: Funktionieren deine Bedingungen aus den Schritten 5, 6 und 7 jetzt 
# noch zuverlässig? Warum nicht?
# Mache aus den ungültigen Bedingungen und den dazu gehörigen prints nun Kommentare.

# Schritt 10
# Wie musst du die Bedingung aus Schritt 5 so anpassen,
# dass sie ein "Unentschieden" immer richtig erkennt?
# Tipp: man kann auch direkt zwei Variablen miteinander vergleichen...

if handThanos == handIronman:
  print ("Es ist unentschieden!")



#############################################################
######  Bonusaufgaben für Programmier-Superheld:innen  ######
#############################################################

# Schritt 11
# Wie musst du die Bedingung aus Schritt 6 so anpassen,
# dass sie ein "Ironman gewinnt" immer richtig erkennt?
# Tipp 1: Man kann die Vergleiche in den Bedingungen mit "and" miteinander 
# verknüpfen, zum Beispiel "if temperature > 20 and rain == 0:"
# Tipp 2: Am besten schreibst du drei Bedingungen: eine für den Fall, dass Ironman
# Schere hat, eine für Stein und eine für Papier


if handIronman=="Schere" and handThanos=="Papier":
  print ("Ironman hat gewonnen!")

if handIronman=="Stein" and handThanos=="Schere":
  print ("Ironman hat gewonnen!")  

if handIronman=="Papier" and handThanos=="Stein":
  print ("Ironman hat gewonnen!")  
  

# Schritt 12
# Wie musst du die Bedingung aus Schritt 6 so anpassen,
# dass sie ein "Thanos gewinnt" immer richtig erkennt?

if handThanos=="Stein" and handIronman=="Schere":
  print ("Thanos hat gewonnen!")

if handThanos=="Papier" and handIronman=="Stein":
  print ("Thanos hat gewonnen!")
  
if handThanos=="Schere" and handIronman=="Papier":
  print ("Thanos hat gewonnen!")

