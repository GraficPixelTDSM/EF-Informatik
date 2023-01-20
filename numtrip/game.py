from random import randint
from math import log
import json  # Importiert "randint", "log" und "json"
MAX_POTENZ_START = 3  # Setzt die maximale Potenz der Zahlen die (anfänglich) generiert werden fest
MAX_POTENZ_VAR = 3  # Setzt die maximale Potenz der Zahlen die (neu) generiert werden fest
WIN_NUM = 128  # Setzt die zu erreichende Zahl fest um das Spiel zu gewinnen
Game_Over = False
loss = False
ok = 0  # Setzt einige Werte für Variabeln fest
dateiname = 'numtrip_safe.json'  # Setzt den Namen der Speicherdatei fest. Gespeichert: "spiel", "ok", "poss_move", "loss"
daten = {}  # Sagt, dass "daten" eine Datensammlung ist
spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]
         for i in range(5)]  # Generiert das anfängliche Spielfeld
anzeige = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]  # Sagt, dass "anzeige" mit '0' gefüllt ist
check = [[], []]  # Sagt, dass "check" eine Liste ist, mit zwei leeren Listen darin
#check= [[y], [x]]


def möglich():  # Definition für die Überprüfung, ob noch ein Zug möglich ist
    global poss_move
    poss_move = False  # "poss_move" wird hier standartmässig auf 'False' gesetzt. Ist ein Zug möglich verändert sich das wieder auf 'True'
    for my in range(5):  # Wiederholt für jede Zeile:
        for mx in range(5):  # Wiederholt für jede Spalte:
            if my > 0:  # Wenn die Zahl darüber,
                if spiel[my][mx] == spiel[my - 1][mx]:
                    poss_move = True
                    return poss_move
            if my < 4:  # darunter,
                if spiel[my][mx] == spiel[my + 1][mx]:
                    poss_move = True
                    return poss_move
            if mx > 0:  # links davon
                if spiel[my][mx] == spiel[my][mx - 1]:
                    poss_move = True
                    return poss_move
            if mx < 4:  # oder rechts davon == die ausgewählte Zahl ist, sollte "poss_move" == 'True' gesetzt und zurückgegeben werden
                if spiel[my][mx] == spiel[my][mx + 1]:
                    poss_move = True
                    return poss_move
            if poss_move == True:
                break  # Anschliessend soll die Schleife abgebrochen werden
        if poss_move == True:
            break


def field_print():  # Definition für die Ausgabe des Spielfeldes
    global daten
    for i in range(5):  # Wiederholt für jede Zeile:
        for j in range(5):  # Wiederholt für jede Spalte:
            global spiel
            # Setzt die Zahl in "spiel[i][j]" in "anzeige[i][j]" ein und füge genügend Leerschläge zu "anzeige[i][j]" ein um ein schönes Spielfeld beizubehalten
            for k in range(5):
                if spiel[i][j] < 10**k:
                    k = 4 - k  # Je nach dem wie viele Stellen die Zahl hat, wird eine unterschiedliche Anzahl an Leerschlägen eingefügt
                    anzeige[i][j] = k * " " + f'{spiel[i][j]}'
                    break
    print('\033[35m' + '    01     02     03     04     05   ' + '\033[39m' +
          '\n ╔══════╤══════╤══════╤══════╤══════╗')  # Druckt den oberen Teil des Spielfeldes
    for i in range(5):  # Wiederholt für jede Zeile:
        def logg(p):  # Je nach dem welche Zahl in "spiel[i][p]" ist, sollte eine Zahl zurückgegeben werden, die dann die Farbe der Zahl festlegt. Die Zahl bzw. die Farbe ist für gleiche Zahlen gleich und die Farbreihe wiederholt sich mit der Zeit, da es nicht unendlich Farben gibt
            # Findet mit "log(int(spiel[i][p])) / log(2)" den Exponenten der Zahl "spiel[i][p]" mit der Basis "2" heraus. Diese Zahl "% 6" ergibt einen Wert zwischen 0 und 5. Diese Zahl "+91" ergibt eine Zahl zwischen 91 und 96. Diese Zahlen richtig eingesetzt führen zu einer Zahl mit den "High Intensty" Farben "Rot, Grün, Gelb, Blau, Lila, Zyan"
            col_num = int(((log(int(spiel[i][p])) / log(2)) % 6) + 91)
            return col_num  # gib die Zahl zurück
        print(" ║      │      │      │      │      ║\n" + '\033[35m' + str(i + 1) + '\033[39m' + "║", f'\033[1;{logg(0)}m' + anzeige[i][0], '\033[0;39m' + "│", f'\033[1;{logg(1)}m' + anzeige[i][1], '\033[0;39m' + "│", f'\033[1;{logg(2)}m' +
              anzeige[i][2], '\033[0;39m' + "│", f'\033[1;{logg(3)}m' + anzeige[i][3], '\033[0;39m' + "│", f'\033[1;{logg(4)}m' + anzeige[i][4], '\033[0;39m' + "║\n" + " ║      │      │      │      │      ║")
        # /\ Drucke eine Zeile des Spielfeldes mit den Zahlen aus
        if i < 4:
            print(" ╟──────┼──────┼──────┼──────┼──────╢")
    print(" ╚══════╧══════╧══════╧══════╧══════╝")  # Drucke den Spielfeldabschluss nach dem Drucken aller Zeilen aus

    daten['spiel'] = spiel  # Speichert die Daten von "spiel" in der Datensammlung als "spiel"
    with open(dateiname, 'w') as f:  # Öffnet die Datensammlung "numtrip_safe.json" und erhalte mit "w" die Schreiberlaubnis
        json.dump(daten, f)  # <- Speichert den Wert "spiel"
    möglich()  # Ruft die Definition zur Prüfung der möglichen Züge
    if poss_move == False:  # Wenn keine Züge mehr möglich sind:
        global Game_Over
        global loss
        Game_Over = True  # Setz "Game_Over" auf 'True', da das Spiel vorbei ist, wenn keine Züge mehr möglich sind
        loss = True  # Setzt "loss" auf 'True'
        high = 0  # Setzt "high" = '0'
        for q in range(5):  # Wiederholt für jede Zeile
            for w in range(5):  # Wiederholt für jede Spalte
                if spiel[q][w] > high:  # Wenn die aktuelle Zahl grösser als die vorher grösste Zahl ist:
                    high = spiel[q][w]  # Setzt die grösste Zahl = der aktuellen Zahl
        for h in range(5):  # Wiederholt für jede Zeile:
            # Wenn die Gewinnzahl (128) in einer Zeile ist, oder die höchste Zahl grösser als die Gewinnzahl ist:
            if WIN_NUM in spiel[h] or high > WIN_NUM:
                loss = False  # Setzt "loss" auf 'False', da man trotzdem gewonnen hat, obwohl man keine Züge mehr hat
        daten['poss_move'] = poss_move  # Setzt "poss_move" in die Datensammlung unter dem Namen "poss_move" ein
        daten['loss'] = loss  # Setzt "loss" in die Datensammlung unter dem Namen "loss" ein
        with open(dateiname, 'w') as f:  # Speichert die Daten in der Datei
            json.dump(daten, f)


möglich()  # Ruft die Definition zur Prüfung der möglichen Züge
while poss_move == False:  # Während kien Zug möglich ist:
    spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]
             for i in range(5)]  # Generiert ein neues Spielfeld, wenn beim alten kein Zug möglich ist
    möglich()  # Ruft die Definition zur Prüfung der möglichen Züge auf

load_game = input('\033[91m' +
                  '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ' + '\033[0m').lower()  # Spielerabfrage, ob ein altes Spiel geladen werden soll
while load_game != 'l' and load_game != 'n':  # Wenn die eingabe nicht den möglichen Antwortmöglichkeiten entspricht:
    load_game = input('\033[91m'
                      '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ' + '\033[0m')  # Erneute Spielerabfrage
if load_game == 'l':  # Wenn das Spiel geladen werden soll:
    try:  # Versuche:
        with open(dateiname) as f:  # Öffne die Datei
            daten = json.load(f)
            spiel = daten['spiel']  # Lädt die vergangene Runde und setzt "spiel" = der als "spiel" gespeicherten Daten
    except:  # Wenn das obere nicht funktioniert, d.h. einen Fehler ergeben würde
        # Informiert den Spieler, dass keine Datei gefunden wurde
        print('[!] Da leider kein gespeichertes Spiel gefunden wurde, wurde ein neues erstellt.')
        load_game = 'n'  # Setzt "load_game" = 'n' damit das Spiel weiss, dass nichts geladen wurde
if load_game == 'l':  # Wenn das Spiel geladen werden soll und wenn das Laden von "spiel" funktioniert hat:
    try:  # Versuche:
        with open(dateiname) as f:  # Lädt den Wert für "loss"
            loss = daten['loss']
    except:  # Wenn "loss" nicht geladen werden kann, d.h. nicht vorhanden ist, d.h. einen Fehler ergeben würde:
        loss = False  # Setzt "loss" auf 'False', man hat das Spiel dann noch nicht verloren
    try:  # Versuche:
        with open(dateiname) as f:  # Lädt den Wert für "poss_move"
            poss_move = daten['poss_move']
    except:  # Wenn "poss_move" nicht geladen werden kann, d.h. nicht vorhanden ist, d.h. einen Fehler ergeben würde:
        poss_move = True  # Wenn "poss_move" nicht gefunden wurde, ist ein Zug noch möglich, d.h. wird "poss_move" = 'True' gesetzt
    if poss_move == False and loss == True:  # Wenn der geladene Spielstand nicht fortführbar und verloren ist:
        field_print()  # Druckt das Spielfeld des vergangenen Spiels
        print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
              f'Willkommen zurück Spieler!\nDas geladene Spiel kann leider nicht fortgeführt werden. Da du die erforderliche Punktzahl nicht erreicht hast, hast du es verloren.\nÜber dieser Nachricht ist aber noch das Spielfeld der vergangenen Runde.\nDarunter wurde ein neues Spiel erstellt.' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
        spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]  # /\ Informiert den Spieler, dass das Spiel vorbei und verloren ist
                 for i in range(5)]  # Generiert ein neues Spielfeld
        möglich()  # Prüft, ob das generiert Spielfeld spielbar ist
        while poss_move == False:  # Wenn das generierte Spielfeld nicht spielbar ist:
            spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]
                     for i in range(5)]  # Generiert ein neues Spielfeld
            möglich()  # Prüft, ob das generiert Spielfeld spielbar ist
    elif poss_move == False and loss == False:  # Wenn der geladene Spielstand nicht fortführbar aber gewonnen ist:
        field_print()  # Druckt das Spielfeld des vergangenen Spiels
        print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
              f'Willkommen zurück Spieler!\nDas geladene Spiel kann leider nicht fortgeführt werden. Da du aber die erforderliche Punktzahl erreicht hast, hast du es gewonnen.\nÜber dieser Nachricht ist aber noch das Spielfeld der vergangenen Runde.\nDarunter wurde ein neues Spiel erstellt.' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
        spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]  # /\ Informiert den Spieler, dass das Spiel vorbei aber gewonnen ist
                 for i in range(5)]  # Generiert ein neues Spielfeld
        möglich()  # Prüft, ob das generiert Spielfeld spielbar ist
        while poss_move == False:  # Wenn das generierte Spielfeld nicht spielbar ist:
            spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]
                     for i in range(5)]  # Generiert ein neues Spielfeld
            möglich()  # Prüft, ob das generiert Spielfeld spielbar ist
    else:  # Andererseits (Wenn noch Züge möglich sind):
        print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
              f'Willkommen zurück Spieler!\nVersuche die Zahl {WIN_NUM} zu erreichen, oder, wenn du das schon geschafft hast, spiele im unbegrenzten Modus weiter.\nDas Spiel speichert automatisch nach jeder Eingabe und kann jederzeit beendet und fortgesetzt werden.\nViel Glück!\n-GPTDSM' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
        # /\ Informiert den Spieler, dass das Spiel weitergeht
if load_game == 'n':  # Wenn das Spiel nicht geladen werden soll:
    print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
          f'Willkommen zu Numtrip! Klicke auf eine Zahl um alle anliegenden, gleichen Zahlen auf diesen Block zusammenzufassen.\nDabei wird der Wert der angeklickten Zahl verdoppelt. Es werden ständig neue Zahlen kommen, sobald du einige zusammenfasst. \nVersuche die Zahl {WIN_NUM} zu erreichen, oder spiele danach im unbegrenzten Modus weiter.\nDas Spiel speichert automatisch nach jeder Eingabe und kann jederzeit beendet und fortgesetzt werden.\nViel Glück!\n-GPTDSM' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
    # Druckt dem Spiler einige Informationen aus, bevor er das Spiel startet


field_print()  # Ruft die Definition zur Ausgabe des Spielfeldes auf


def main():  # Definiert die Hauptschleife
    global Game_Over
    Game_Over = False  # Anfangs jeder Schleife wird "game_over" auf 'False' gesetzt
    while Game_Over is False:  # Führt aus, solange "Game_Over" 'False' ist:
        def check_num_input(inp):  # Definition zur Überprüfung, ob eine Eingabe gültig ist
            if inp.isnumeric():  # Es sollte eine Zahl sein
                if int(inp) <= 5 and int(inp) >= 1:  # Die Zahl sollte zwischen 1 und 5 sein
                    return True  # Wenn die Zahl zwischen 1 und 5 ist, wird 'True' zurückgegeben
                else:  # Sonst
                    # Informiert den Spieler, dass seine Eingabe ungültig ist
                    print('\033[91m' + '[!] Bitte schreibe eine Zahl zwischen 1 und 5!' + '\033[0m')
                    return False  # Da die Zahl nicht zwischern 1 und 5 ist, wird 'False' zurückgegeben
            else:
                # Wenn die Eingabe keine Zahl ist, wird der Spieler informiert und 'False' zurückgegeben
                print('\033[91m' + '[!] Bitte schreibe eine (positive) Zahl!' + '\033[0m')
                return False
        global x_a
        global y_a
        global ok
        x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')  # Es wird nach einer Eingabe gefragt
        while check_num_input(x_a) is False:
            # Die Frage wird erneut gestellt, wenn die Prüfung "False" zurückgibt
            x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')
        check[0].append(x_a)  # Fügt die Eingabe zu den zu prüfenden Koordinaten an
        y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')  # Es wird nach einer Eingabe gefragt
        while check_num_input(y_a) is False:
            # Die Frage wird erneut gestellt, wenn die Prüfung "False" zurückgibt
            y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')
        check[1].append(y_a)  # Fügt die Eingabe zu den zu prüfenden Koordinaten an
        if load_game == 'l':  # Wenn ein Spielstand geladen werden soll:
            try:  # Versucht den gespeicherten Wert für "ok" zu laden
                with open(dateiname) as f:
                    daten = json.load(f)
                    global ok
                    ok = daten['ok']
            except:  # Sonst:
                ok = 0  # Setzt "ok" = '0'

        if ok == 0:  # Wenn "ok" == '0' ist (noch nicht im unbegrenzten Modus):
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' +
                  y_a + ')' + '\033[0m')  # Druckt die gewählte Koordinate aus
        elif ok == 1:  # Wenn "ok" == '1' ist (im unbegrenzten Modus):
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' +
                  y_a + ')' + '\033[91m' + ' (Unbegrenzter Modus)' + '\033[0m')  # Druckt die gewählte Koordinate und eine Info über den Modus aus
        x_a = int(x_a) - 1  # Verringert den Input um 1 um ihn auf Listen anwenden zu können
        y_a = int(y_a) - 1
        tempa = 0
        found = False  # setze "tempa" und "found" fest
        # "check" ist eine Liste von Koordinaten, bei denen noch überprüft werden soll, ob gleiche Zahlen daneben sind. Wenn Zahlen zu prüfen sind:
        while len(check[0]) > 0:
            tempa = +1  # "tempa" sollte bei jeder Wiederholung grösser werden
            for v in range(len(check[0])):  # Wiederholt für jede zu prüfende Koordinate:
                x = int(check[0][0]) - 1
                y = int(check[1][0]) - 1  # Verringert den Wert um 1 um ihn auf Listen anwenden zu können
                if tempa < 2:  # Da "tempa" bei jeder Widerholung grösser wird, sollte und wird diese Funktion nur einmal ausgeführt
                    # Hier wird der Zahlenwert aus der Anzeige (ohne Leerzeichen) extrahiert. Die Zahlen werden aus der Anzeige genommen um sicherzustellen, dass es sich um die dem Spieler angezeigten Werte handelt
                    anz3 = int(anzeige[y_a][x_a].strip())

                # Entfernt die je vorderste Zahl der Liste, damit bei der nächsten Wiederholung die nächste Zahl genommen wird
                check[0].pop(0)
                check[1].pop(0)  # Die entfernten Zahlen wurden vorher schon zwischengespeichert
                if x < 4:  # Diese Funktion prüft, ob eine Zahl rechts vom Startpunkt ist. Wenn x < 4 ist, ist dort ganz sicher eine Zahl. Wenn x !< 4 ist, sind wir am Rand des Spielfeldes, was heisst, dass dor keine Zahl sein kann
                    anz1 = int(anzeige[y][x + 1].strip())  # "anz1" erhält den Wert der rechten Zahl
                    anz2 = int(anzeige[y][x].strip())  # "anz2" erhält den Wert der gewählten Zahl
                    # Wenn die beiden Werte (gewählte Zahl / rechte Zahl) übereinstimmen, wird ausgeführt:
                    if anz2 == anz1:
                        # Wenn die rechte Zahl nicht "0" ist, d.h. schon überprüft wurde, führe aus:
                        if spiel[y][x + 1] != 0:
                            # Fügt die x-Koordinate der ausgewählten Zahl zu "check[0]" an aber gibt +2 (+1 +1) hinzu (für 'rechts davon' und um sie einem Input-format anzupassen)
                            check[0].append(x + 2)
                            # Fügt die y-Koordinate der ausgewählten Zahl zu "check[1]" an aber gibt +1 hinzu (um sie einem Inputformat anzupassen)
                            check[1].append(y + 1)
                            # Setzt die Zahl rechts der Auswahl auf "0", damit sie nicht nochmal geprüft wird (kann zu einem Loop führen)
                            spiel[y][x + 1] = 0
                            found = True  # Sobald eine gleiche Zahl im Umkreis gefunden wurde wird "found" auf 'True' gesetzt
                if x > 0:  # Die gleiche Prozedur gilt für Zahlen links der Auswahl
                    anz1 = int(anzeige[y][x - 1].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y][x - 1] != 0:
                            check[0].append(x)
                            check[1].append(y + 1)
                            spiel[y][x - 1] = 0
                            found = True
                if y < 4:  # Die gleiche Prozedur gilt für Zahlen unter der Auswahl
                    anz1 = int(anzeige[y + 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y + 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y + 2)
                            spiel[y + 1][x] = 0
                            found = True
                if y > 0:  # Die gleiche Prozedur gilt für Zahlen über der Auswahl
                    anz1 = int(anzeige[y - 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y - 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y)
                            spiel[y - 1][x] = 0
                            found = True
        if found is True:  # Diese Funktion sollte nur ausgeführt werde, wenn eine gleiche Zahl im Umkreis der Auswahl gefunden wurde, d.h. wenn "found" == 'True' ist
            spiel[y_a][x_a] = anz3 * 2  # Verdoppelt die Ausgewählte Zahl

        # Führt aus, solange 0 in irgendeiner Zeile ist
        while 0 in spiel[0] or 0 in spiel[1] or 0 in spiel[2] or 0 in spiel[3] or 0 in spiel[4]:
            for l in range(5):  # Führt für jede Zeile aus
                for m in range(5):  # Führt für jede Spalte aus
                    if spiel[l][m] == 0:  # Führt aus, wenn die Zahl == 0 ist:
                        # Führt aus, wenn "l" == '0' bzw. "y" == '0' (die Zahl also am ganz oberen Rand ist):
                        if l == 0:
                            # Generiert eine zufällige, neue Zahl für "spiel[0][m]"
                            spiel[0][m] = 2**randint(1, MAX_POTENZ_VAR)
                        else:  # Führt aus, wenn nicht am oberen Rand:
                            spiel[l][m] = spiel[l - 1][m]  # Gibt der aktuellen Zahl den Wert der oberen
                            spiel[l - 1][m] = 0  # Setzt den Wert der oberen Zahl auf '0'
        if load_game == 'l':  # Wenn ein Spielstand geladen werden soll:
            try:  # Es wird versucht den gespeicherten Wert für "ok" zu laden
                with open(dateiname) as f:
                    daten = json.load(f)
                    ok = daten['ok']
            except:  # Sonst wird "ok" = '0'
                ok = 0
        # wenn "ok" == 0 sollte für jede Zeile überprüft werden, ob die, für den Sieg notwendige Zahl (128) erreicht ist
        if ok == 0:
            for l in range(5):
                if WIN_NUM in spiel[l]:
                    # Wenn die für den Sieg notwendige Zahl (128) erreicht ist, setze "Game_Over" = True
                    Game_Over = True

        field_print()  # Ruft die Funktion auf, zum Drucken des Spielfeldes


main()  # Rufe die Funktion auf, zum starten des Hauptloops
if Game_Over == True:  # Wird ausgeführt, wenn das Spiel vorbei ist:
    if poss_move == True:  # Wenn Züge noch möglich sind:
        weiter = input(
            '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
        # Der Spieler wird gefragt, wie er fortfahren will
        weiter = weiter.lower()  # Die Eingabe wird in Kleinbuchsteben gesetzt
        while weiter != 'ja' and weiter != 'j' and weiter != 'y' and weiter != 'yes' and weiter != 'nein' and weiter != 'n' and weiter != 'no':
            # Solange keine Antwort gültig ist, wird nochmal gefragt
            print('\033[91m' + "[!] Bitte gib eine gültige Antwort ein! (Gültige Antworten: 'j', 'ja', 'y', 'yes', 'n', 'nein', 'no')" + '\033[0m')
            weiter = input(
                '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
            weiter = weiter.lower()

        if weiter == 'ja' or weiter == 'j' or weiter == 'y' or weiter == 'yes':  # Wenn weitergespielt werden soll:
            # "ok" wird = '1' gesetzt, was dazu führt, dass die Siegbedingung (WIN_NUM = 128) nicht mehr geprüft wird
            ok = 1
            daten['ok'] = ok  # Speichert "ok", damit die Siegbedingung nicht mehr geprüft wird, wenn ein Spiel geladen wird
            with open(dateiname, 'w') as f:
                json.dump(daten, f)
            main()  # "main()" wird "Game_Over" = 'False' setzen und nie mehr auf True setzen, was den Modus unbegrenzt macht, solange Züge möglich sind
        elif weiter == 'nein' or weiter == 'n' or weiter == 'no':  # Wenn nicht weitergespielt werden soll:
            Game_Over = True  # Setzt "Game_Over" zur Sicherheit nochmals auf True
            # Druckt die finale Nachricht aus
            print('\033[94m' + "\n[!] Danke für's Spielen von Numtrip.\n-GPTDSM\n" + '\033[0m')
    if poss_move == False:
        print(
            '\033[93m' + f'[!] Das Spiel ist in diesem Zustand leider nicht mehr fortführbar.' + '\033[0m')
        # Benachrichtigt, dass kein Zug mehr möglich ist
        high = 0  # Setzt "high" = '0'
        for q in range(5):  # Wiederholt für jede Zeile
            for w in range(5):  # Wiederholt für jede Spalte
                if spiel[q][w] > high:  # Wenn die aktuelle Zahl grösser als die vorher grösste Zahl ist:
                    high = spiel[q][w]  # Setzt die grösste Zahl = der aktuellen Zahl
        if loss == False:
            print(
                '\033[93m' + f"Du hast aber die erforderliche Punktzahl von {high} erreicht. Das Heisst, du gewinnst das Spiel.\nDanke für's Spielen von Numtrip.\n-GPTDSM\n" + '\033[0m')
            # Wenn die Siegbedingung erfüllt ist, informiere den Spieler
        if loss == True:
            print(
                '\033[93m' + f"Du hast die erforderliche Punktzahl von {WIN_NUM} nicht erreicht. Das Heisst, du verlierst das Spiel.\nDanke für's Spielen von Numtrip.\n-GPTDSM\n" + '\033[0m')
            # Wenn die Siegbedingung nicht erfüllt ist, informiere den Spieler
# GPTDSM
# ANSI Code '\033[X;XXm' for Color: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
