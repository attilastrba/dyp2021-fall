# Diese Programmierübung handelt davon, wie Thanos nach den Infinity Steinen sucht.
# Diese ersten drei Zeilen bereiten die Grafiken von Thanos und der Karte vor.
# Sie sollten unverändert ganz am Anfang des Programms stehen.
import thanosMap
map = thanosMap.map()
thanos = thanosMap.thanos(map.screen)

# SCHRITT 1
# Das Programm besteht bisher nur aus drei Zeilen. Führe es aus und
# sieh nach, was passiert.

# SCHRITT 2
# Frage den Anwender nach dem Namen des Planeten, auf dem Thanos nach den Steinen sucht. Benutze dafür die input() Funktion.
# Speichere das Ergebnis in der Variablen 'planet'

planet = input("Auf welchem Planeten ist Thanos? ")

# SCHRITT 3
# Gib auf dem Bildschirm aus, auf welchem Planeten Thanos jetzt gelandet ist.
# Verwende dafür die print() Funktion und die Variable 'planet'.

print("Thanos ist jetzt auf dem Planeten " + planet + " gelandet!")

# SCHRITT 4
# Jetzt soll Thanos sich auf der Karte bewegen. Er geht nach Norden, wenn
# den Befehl 'thanos.goNorth()' eingibst. In den Klammern kannst du ALS ZAHL angeben,
# wie weit Thanos gehen soll.
# Ein graues Kästchen auf der Karte entspricht 10 Kilometern.
# Bewege Thanos 5km nach Norden.

thanos.goNorth(5)

# SCHRITT 5
# Probiere auch die anderen Himmelsrichtungen aus. Benutze
# thanos.goWest()
# thanos.goSouth()
# thanos.goEast()

thanos.goWest(5)
thanos.goSouth(5)
thanos.goEast(5)

# SCHRITT 6
# Ab jetzt soll der Anwender bestimmen, wohin Thanos geht.
# Mache alle Bewegungs-Zeilen (z.B. 'thanos.goNorth()') zu Kommentaren, indem du ein '#'-Zeichen davor schreibst)

# SCHRITT 7
# Thanos macht sich auf die Suche nach dem ersten Stein.
# Frage den Anwender, wie weit Thanos nach NORDEN gehen soll.
# Speichere das Ergebnis in der Variablen 'streckeNord'

streckeNord = input("Wie weit soll Thanos nach Norden gehen? ")

# SCHRITT 8
# Gib auf dem Bildschirm als Bestätigung aus, wie weit Thanos nach Norden gehen soll.
# Benutze dafür wieder die print() Funktion.

print("OK, Thanos geht " + streckeNord + " nach Norden.")

# SCHRITT 9
# Lasse Thanos die eingegebene Strecke nach Norden laufen.
# Benutze wieder den Befehl 'thanos.goNorth()' und die Variable 'streckeNord'.
# Tipp: mit der Funktion int() kannst du deine Variable
# von einem String in eine Zahl umwandeln.

thanos.goNorth(int(streckeNord))

# SCHRITT 10
# Frage den Anwender, wie weit Thanos nach WESTEN gehen soll.
# Speichere das Ergebnis in der Variablen 'streckeWest'.
# Bewege Thanos der Eingabe entsprechend nach Westen.

streckeWest = input("Wie weit soll Thanos nach Westen gehen? ")
thanos.goWest(int(streckeWest))

# SCHRITT 11
# Frage den Anwender, wie weit Thanos nach SÜDEN gehen soll.
# Speichere das Ergebnis in der Variablen 'streckeSued'.
# Bewege Thanos der Eingabe entsprechend nach Süden.

streckeSued = input("Wie weit soll Thanos nach Süden gehen? ")
thanos.goSouth(int(streckeSued))

# SCHRITT 12
# Frage den Anwender, wie weit Thanos nach OSTEN gehen soll.
# Speichere das Ergebnis in der Variablen 'streckeOst'.
# Bewege Thanos der Eingabe entsprechend nach Osten.

streckeOst = input("Wie weit soll Thanos nach Osten gehen? ")
thanos.goEast(int(streckeOst))

# SCHRITT 13
# Rechne aus, wie weit Thanos insgesamt gegangen ist.
# Gib das Ergebnis auf dem Bildschirm aus.
# Tipp: mit der Funktion str() kannst du eine Zahl in einen String umwandeln.

streckeGesamt = int(streckeNord) + int(streckeWest) + int(streckeSued) + int(
    streckeOst)

print("Thanos geht insgesamt " + str(streckeGesamt) + " Kilometer")


# SCHRITT 14
# Thanos kann 6km pro Stunde gehen.
# Lass auf dem Bildschirm ausgeben, wie viele Stunden er insgesamt unterwegs ist.
# Dazu musst du die Variable streckeGesamt durch die Gehgeschwindigkei teilen.
# Zum Teilen kannst du in Python den Operator / benutzen.

dauerGesamt = streckeGesamt / 6
print ("Thanos Reise dauert " + str(dauerGesamt) + " Stunden.")