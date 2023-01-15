from random import randint
from math import log
import json  # Importiere "randint", "log" und "json"
MAX_POTENZ_START = 5  # setzt die maximale Potenz der Zahlen die (anfänglich) generiert werden fest
MAX_POTENZ_VAR = 2  # setzt die maximale Potenz der Zahlen die (neu) generiert werden fest
WIN_NUM = 128  # setzt die zu erreichende Zahl fest um das Spiel zu gewinnen
Game_Over = False
ok = 0
wl = 0  # setzt einige Werte für Variabeln ein
dateiname = 'numtrip_safe.json'  # setzt den Namen der Speicherdatei fest. Gespeichert: spiel, wl, ok
daten = {}  # -> sagt, dass "daten" eine Datensammlung ist
spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]
         for i in range(5)]  # generiere das anfängliche Spielfeld
anzeige = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]  # sage, dass "anzeige" mit "0" gefüllt ist
check = [[], []]  # sage, dass "check" eine Liste ist, mit zwei leeren Listen darin
#check= [[y], [x]]

load_game = input(
    '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ').lower()  # frage ob ein altes Spiel geladen werden soll
while load_game != 'l' and load_game != 'n':
    load_game = input(
        '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ')  # frage erneut, wenn die eingabe nicht den möglichen Antwortmöglichkeiten entspricht
if load_game == 'l':
    try:
        with open(dateiname) as f:
            daten = json.load(f)
            spiel = daten['spiel']  # lade eine vorhandene Spieldatei wenn "l" ausgewählt wurde
    except:
        # Wenn keine Spieldatei vorhanden ist, informiere den Spieler und generiere ein neues Spiel
        print('[!] Da leider kein gespeichertes Spiel gefunden wurde, wurde ein neues erstellt.')
print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
      f'Willkommen zu Numtrip! Klicke auf eine Zahl um alle anliegenden, gleichen Zahlen auf diesen Block zusammenzufassen.\nDabei wird der Wert der angeklickten Zahl verdoppelt. Es werden ständig neue Zahlen kommen, sobald du einige zusammenfasst. \nVersuche die Zahl {WIN_NUM} zu erreichen, oder spiele danach im unbegrenzten Modus weiter.\nDas Spiel speichert automatisch nach jeder Eingabe und kann jederzeit beendet und fortgesetzt werden.\nViel Glück!\n-GPTDSM' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
# drucke dem Spiler einige Informationen aus, bevor er das Spiel startet


def field_print():  # Definition für die Ausgabe des Spielfeldes
    global daten
    for i in range(5):  # führe für jede Zeile aus:
        for j in range(5):  # führe für jede Spalte aus:
            global spiel
            # setze die Zahl in "spiel[i][j]" in anzeige[i][j]" ein und füge genügend Leerschläge zu "anzeige[i][j]" ein um ein schönes Spielfeld beizubehalten
            for k in range(4):
                if spiel[i][j] < 10**k:
                    k = 4 - k  # je nach dem wie viele Stellen die Zahl hat, wird eine unterschiedliche Anzahl an Leerschlägen eingefügt
                    anzeige[i][j] = k * " " + f'{spiel[i][j]}'
                    break
    print('\033[35m' + '    01     02     03     04     05   ' + '\033[39m' +
          '\n ╔══════╤══════╤══════╤══════╤══════╗')  # drucke den oberen Teil des Spielfeldes
    for i in range(5):  # wiedderhole für jede Zeile:
        def logg(p):  # je nach dem welche Zahl in "spiel[i][p-1]" sollte eine Zahl zurückgegeben werden, die dann die Farbe der Zahl festlegt. Die Zahl bzw. die Farbe ist für gleiche Zahlen gleich und die Farbreihe wiederholt sich mit der Zeit, da es nicht unendliche Zahlen gibt
            # finde mit "log(int(spiel[i][p])) / log(2)" den Exponenten der Zahl "spiel[i][p]" mit der Basis "2" heraus. Diese Zahl "% 6" ergibt einen Wert zwischen 0 und 5. Diese Zahl "+91" ergibt eine Zahl zwischen 91 und 96. Diese Zahlen richtig eingesetzt führen zu einer Zahl mit den "High Intensty" Farben "Rot, Grün, Gelb, Blau, Lila, Zyan"
            col_num = int(((log(int(spiel[i][p])) / log(2)) % 6) + 91)
            return col_num  # gib die Zahl zurück
        print(" ║      │      │      │      │      ║\n" + '\033[35m' + str(i + 1) + '\033[39m' + "║", f'\033[1;{logg(0)}m' + anzeige[i][0], '\033[0;39m' + "│", f'\033[1;{logg(1)}m' + anzeige[i][1], '\033[0;39m' + "│", f'\033[1;{logg(2)}m' +
              anzeige[i][2], '\033[0;39m' + "│", f'\033[1;{logg(3)}m' + anzeige[i][3], '\033[0;39m' + "│", f'\033[1;{logg(4)}m' + anzeige[i][4], '\033[0;39m' + "║\n" + " ║      │      │      │      │      ║")
        # /\ Drucke eine Zeile des Spielfeldes mit den Zahlen aus
        if i < 4:
            print(" ╟──────┼──────┼──────┼──────┼──────╢")
    print(" ╚══════╧══════╧══════╧══════╧══════╝")  # Drucke den Spielfeldabschluss nach dem Drucken aller Zeilen aus
    daten['spiel'] = spiel  # speichere die Daten von "spiel" in der Datensammlung als "spiel"
    with open(dateiname, 'w') as f:  # öffne die Datensammlung "numtrip_safe.json" und erhalte mit "w" die Schreiberlaubnis
        json.dump(daten, f)  # <- Speichere den Wert "spiel"


field_print()  # rufe die Definition zur Ausgabe des Spielfeldes auf


def main():
    global Game_Over
    Game_Over = False
    while Game_Over is False:  # Führe aus, solange "Game_Over" "False" ist:
        def check_num_input(inp):  # Definition zur Überprüfung, ob eine Eingabe gültig ist
            if inp.isnumeric():  # Es sollte eine Zahl sein
                if int(inp) <= 5 and int(inp) >= 1:  # Die Zahl sollte zwischen 1 und 5 sein
                    return True
                else:
                    print('\033[91m' + '[!] Bitte schreibe eine Zahl zwischen 1 und 5!' + '\033[0m')
                    return False
            else:
                # Wenn die Kriterien nicht zutreffen wird der Spieler informiert und "False" zurückgegeben
                print('\033[91m' + '[!] Bitte schreibe eine (positive) Zahl!' + '\033[0m')
                return False
        global x_a
        global y_a
        global wl
        x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')  # Frage nach einer Eingabe
        while check_num_input(x_a) is False:
            # Frage erneut, wenn die Prüfung "False" zurückgibt
            x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')
        check[0].append(x_a)
        y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')
        while check_num_input(y_a) is False:
            y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')
        check[1].append(y_a)
        if wl == 0:
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' +
                  y_a + ')' + '\033[0m')  # Drucke die gewählte Koordinate aus
        elif wl == 1:
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' +
                  y_a + ')' + '\033[91m' + ' (Unbegrenzter Modus)' + '\033[0m')
        x_a = int(x_a) - 1  # verringere den Input um 1 um ihn auf Listen anwenden zu können
        y_a = int(y_a) - 1
        tempa = 0
        found = False  # setze "tempa" und "tempb" fest
        while len(check[0]) > 0:  # "check" ist eine Liste von Koordinaten, bei denen noch überprüft werden soll, ob gleiche Zahlen daneben sind
            tempa = +1  # "tempa" sollte bei jeder Wiederholung grösser werden
            for lenc in range(len(check[0])):
                x = int(check[0][0]) - 1
                y = int(check[1][0]) - 1  # verringere den Wert um 1 um ihn auf Listen anwenden zu können
                if tempa < 2:  # da "tempa" bei jeder Widerholung grösser wird, sollte und wird diese Funktion nur einma ausgeführt
                    # Hier wird der Zahlenwert aus der Anzeige (ohne Leerzeichen) extrahiert. Die Zahlen werden aus der Anzeige genommen um sicherzustellen, dass es sich um die dem Spieler angezeigten Werte handelt
                    anz3 = int(anzeige[y_a][x_a].strip())

                # entferne die je vorderste Zahl der Liste, damit bei der nächsten Wiederholung die nächste Zahl genommen wird
                check[0].pop(0)
                check[1].pop(0)  # die entfernten Zahlen wurden vorher schon zwischengespeichert
                if x < 4:  # Diese Funktion prüft, ob eine Zahl rechts vom Startpunkt ist. Wenn x < 4 ist, ist dort ganz sicher eine Zahl. Wenn x !< 4 ist, sind wir am Rand des Spielfeldes, was heisst, dass dor keine Zahl sein kann
                    anz1 = int(anzeige[y][x + 1].strip())  # "anz1" erhält den Wert der rechten Zahl
                    anz2 = int(anzeige[y][x].strip())  # "anz2" erhält den Wert der gewählten Zahl
                    if anz2 == anz1:  # wenn die beiden Werte (gewählte Zahl / rechte Zahl) übereinstimmen, führe aus:
                        # wenn die rechte Zahl nicht "0" ist, d.h. schon überprüft wurde, führe aus:
                        if spiel[y][x + 1] != 0:
                            # füge die x-Koordinate der ausgewählten Zahl zu "check[0]" an aber füge +2 (+1 +1) hinzu (für 'rechts davon' und um sie einem Inputformat anzupassen)
                            check[0].append(x + 2)
                            # füge die y-Koordinate der ausgewählten Zahl zu "check[1]" an aber füge +1 hinzu (um sie einem Inputformat anzupassen)
                            check[1].append(y + 1)
                            # sezte die Zahl rechts der Auswahl auf "0", damit sie nicht nochmal geprüft wird (kann zu einem Loop führen)
                            spiel[y][x + 1] = 0
                            found = True  # Sobald eine gleiche Zahl im Umkreis gefunden wurde wird "tempb" auf "True" gesetzt
                if x > 0:  # die gleiche Prozedur gilt für Zahlen links der Auswahl
                    anz1 = int(anzeige[y][x - 1].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y][x - 1] != 0:
                            check[0].append(x)
                            check[1].append(y + 1)
                            spiel[y][x - 1] = 0
                            found = True
                if y < 4:  # die gleiche Prozedur gilt für Zahlen unter der Auswahl
                    anz1 = int(anzeige[y + 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y + 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y + 2)
                            spiel[y + 1][x] = 0
                            found = True
                if y > 0:  # die gleiche Prozedur gilt für Zahlen über der Auswahl
                    anz1 = int(anzeige[y - 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y - 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y)
                            spiel[y - 1][x] = 0
                            found = True
        if found is True:  # diese Funktion sollte nur ausgeführt werde, wenn eine gleiche Zahl im Umkreis der Auswahl gefunden wurde, d.h. wenn "found" == True ist
            spiel[y_a][x_a] = anz3 * 2  # verdopple die Ausgewählte Zahl

        # führe aus, solange 0 in irgendeiner Zeile ist
        while 0 in spiel[0] or 0 in spiel[1] or 0 in spiel[2] or 0 in spiel[3] or 0 in spiel[4]:
            for l in range(5):  # führe für jede Zeile aus
                for m in range(5):  # führe für jede Spalte aus
                    if spiel[l][m] == 0:  # führe aus, wenn die Zahl == 0 ist:
                        if l == 0:  # führe aus, wenn l == 0 bzw. y == 0 (die Zahl also am ganz oberen Rand ist):
                            # generiere eine zufällige, neue Zahl für "spiel[0][m]"
                            spiel[0][m] = 2**randint(1, MAX_POTENZ_VAR)
                        else:  # führe aus, wenn nicht am oberen Rand:
                            spiel[l][m] = spiel[l - 1][m]  # gib der aktuellen Zahl den Wert der oberen
                            spiel[l - 1][m] = 0  # setze den Wert der oberen Zahl auf 0
        wl = 0  # setze wl = 0
        if load_game == 'l':  # wenn ein Spielstand geladen werden soll:
            try:  # versuche den gespeicherten Wert für "ok" zu laden
                global ok
                with open(dateiname) as f:
                    daten = json.load(f)
                    ok = daten['ok']
            except:  # sonst setzt "ok" = 0
                ok = 0
        # wenn "ok" == 0 sollte für jede Zeile überprüft werden, ob die 'Wincondition' (standartmässig die Zahl 128) erfüllt ist
        if ok == 0:
            for l in range(5):
                if WIN_NUM in spiel[l]:
                    Game_Over = True  # wenn sie erfüllt ist, setze "Game_Over" = True

        field_print()


main()
if Game_Over == True:  # führe aus, wenn das Spiel vorbei ist:
    weiter = input(
        '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
    # frage wie der Spieler fortfahren will
    weiter = weiter.lower()  # die Eingabe wird in Kleinbuchsteben gesetzt
    while weiter != 'ja' and weiter != 'j' and weiter != 'y' and weiter != 'yes' and weiter != 'nein' and weiter != 'n' and weiter != 'no':
        # solange keine Antwort gültig ist, frage nochmal
        print('\033[91m' + "[!] Bitte gib eine gültige Antwort ein! (Gültige Antworten: 'j', 'ja', 'y', 'yes', 'n', 'nein', 'no')" + '\033[0m')
        weiter = input(
            '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
        weiter = weiter.lower()

    if weiter == 'ja' or weiter == 'j' or weiter == 'y' or weiter == 'yes':  # wenn weitergespielt werden soll:
        ok = 1  # setze "ok" = 1, was dazu führt, dass die Wincondition nicht mehr geprüft wird
        daten['ok'] = ok  # speichere "ok", damit die Wincondition nicht mehr geprüft wird, wenn ein Spiel geladen wird
        with open(dateiname, 'w') as f:
            json.dump(daten, f)
        main()  # "main()" wird "Game_Over" = False setzen und nie mehr auf True setzen, was den Modus unbegrenzt macht
    elif weiter == 'nein' or weiter == 'n' or weiter == 'no':  # wenn nicht weitergespielt werden soll:
        Game_Over = True  # setze "Game_Over" zur Sicherheit nochmals auf True
        # Drucke finale Nachricht aus und rufe "main()" nicht mehr auf
        print('\033[94m' + "\n[!] Danke für's Spielen von Numtrip.\n-GPTDSM\n" + '\033[0m')
# TDSM
# ANSI Code '\033[X;XXm' for Color: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
