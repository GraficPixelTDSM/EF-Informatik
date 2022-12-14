from random import randint
from math import log
import json
daten = {}
MAX_POTENZ_START = 2
MAX_POTENZ_VAR = 2
WIN_NUM = 128
Game_Over = False
ok = 0
wl = 0
dateiname = 'numtrip.json'
# Gespeichert: spiel, wl, ok
daten = {}
spiel = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)] for i in range(5)]
anzeige = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
check = [[0], [0]]
#check= [[y], [x]]

load_game = input(
    '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ').lower()
while load_game != 'l' and load_game != 'n':
    load_game = input(
        '[?] Willst du die vorherige Sitzung laden oder ein neues Spiel anfangen? (Laden: L; Neues Spiel: N) ')
if load_game == 'l':
    try:
        with open(dateiname) as f:
            daten = json.load(f)
            spiel = daten['spiel']
    except:
        print('[!] Da leider kein gespeichertes Spiel gefunden wurde, wurde ein neues erstellt.')
print('\n' + '\033[33m' + '════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n\n' + '\033[96m' +
      f'Willkommen zu Numtrip! Klicke auf eine Zahl um alle anliegenden, gleichen Zahlen auf diesen Block zusammenzufassen.\nDabei wird der Wert der angeklickten Zahl verdoppelt. Es werden ständig neue Zahlen kommen, sobald du einige zusammenfasst. \nVersuche die Zahl {WIN_NUM} zu erreichen, oder spiele danach im unbegrenzten Modus weiter.\nDas Spiel speichert automatisch nach jeder Eingabe und kann jederzeit beendet und fortgesetzt werden.\nViel Glück!\n-GPTDSM' + '\033[33m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')


def field_print():
    global daten
    for i in range(5):
        for j in range(5):
            global spiel
            for k in range(4):
                if spiel[i][j] < 10**k:
                    k = 4 - k
                    anzeige[i][j] = k * " " + f'{spiel[i][j]}'
                    break
    print('\033[35m' + '    01     02     03     04     05   ' + '\033[39m' + '\n ╔══════╤══════╤══════╤══════╤══════╗')
    for i in range(5):
        def logg(p):
            pn = int(((log(int(spiel[i][(p - 1)])) / log(2)) % 5) + 92)
            return pn
        print(" ║      │      │      │      │      ║\n" + '\033[35m' + str(i + 1) + '\033[39m' + "║", f'\033[1;{logg(1)}m' + anzeige[i][0], '\033[0;39m' + "│", f'\033[1;{logg(2)}m' + anzeige[i][1], '\033[0;39m' + "│", f'\033[1;{logg(3)}m' +
              anzeige[i][2], '\033[0;39m' + "│", f'\033[1;{logg(4)}m' + anzeige[i][3], '\033[0;39m' + "│", f'\033[1;{logg(5)}m' + anzeige[i][4], '\033[0;39m' + "║\n" + " ║      │      │      │      │      ║")
        if i < 4:
            print(" ╟──────┼──────┼──────┼──────┼──────╢")
    print(" ╚══════╧══════╧══════╧══════╧══════╝")
    daten['spiel'] = spiel
    with open(dateiname, 'w') as f:
        json.dump(daten, f)


field_print()


def main():
    global Game_Over
    Game_Over = False
    while Game_Over is False:
        def check_num_input(inp):
            if inp.isnumeric():
                if int(inp) <= 5 and int(inp) >= 1:
                    return True
                else:
                    print('\033[91m' + '[!] Bitte schreibe eine Zahl zwischen 1 und 5!' + '\033[0m')
                    return False
            else:
                print('\033[91m' + '[!] Bitte schreibe eine (positive) Zahl!' + '\033[0m')
                return False
        global x_a
        global y_a
        global wl
        x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')
        while check_num_input(x_a) is False:
            x_a = input('[?] Welche Position auf der X-Achse willst du auswählen? ')
        check[0].append(x_a)
        y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')
        while check_num_input(y_a) is False:
            y_a = input('[?] Welche Position auf der Y-Achse willst du auswählen? ')
        check[1].append(y_a)
        if wl == 0:
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' + y_a + ')' + '\033[0m')
        elif wl == 1:
            print('\033[92m' + '[!] Ausgewählte Koordinate: (' + x_a + ';' + y_a + ')' +
                  '\033[91m' + ' (Unbegrenzter Modus)' + '\033[0m')
        x_a = int(x_a) - 1
        y_a = int(y_a) - 1
        tempa = 0
        tempb = 0
        while len(check[0]) > 1:
            tempa = +1
            for lenc in range(len(check[0]) - 1):
                global isit
                isit = 0
                x = int(check[0][1]) - 1
                y = int(check[1][1]) - 1
                if tempa < 2:
                    anz3 = int(anzeige[y_a][x_a].strip())

                check[0].pop(1)
                check[1].pop(1)
                if x < 4:
                    anz1 = int(anzeige[y][x + 1].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y][x + 1] != 0:
                            check[0].append(x + 2)
                            check[1].append(y + 1)
                            spiel[y][x + 1] = 0
                            isit = +1
                            tempb = 1
                if x > 0:
                    anz1 = int(anzeige[y][x - 1].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y][x - 1] != 0:
                            check[0].append(x)
                            check[1].append(y + 1)
                            spiel[y][x - 1] = 0
                            isit = +1
                            tempb = 1
                if y < 4:
                    anz1 = int(anzeige[y + 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y + 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y + 2)
                            spiel[y + 1][x] = 0
                            isit = +1
                            tempb = 1
                if y > 0:
                    anz1 = int(anzeige[y - 1][x].strip())
                    anz2 = int(anzeige[y][x].strip())
                    if anz2 == anz1:
                        if spiel[y - 1][x] != 0:
                            check[0].append(x + 1)
                            check[1].append(y)
                            spiel[y - 1][x] = 0
                            isit = +1
                            tempb = 1
        if tempb == 1:
            spiel[y_a][x_a] = anz3 * 2

        while 0 in spiel[0] or 0 in spiel[1] or 0 in spiel[2] or 0 in spiel[3] or 0 in spiel[4]:
            for l in range(5):
                for m in range(5):
                    if spiel[l][m] == 0:
                        if l == 0:
                            spiel[l][m] = 2**randint(1, MAX_POTENZ_VAR)
                        else:
                            spiel[l][m] = spiel[l - 1][m]
                            spiel[l - 1][m] = 0
        wl = 0
        if load_game == 'l':
            try:
                global ok
                with open(dateiname) as f:
                    daten = json.load(f)
                    ok = daten['ok']
            except:
                ok = 0
        if ok == 0:
            for l in range(5):
                if WIN_NUM in spiel[l]:
                    Game_Over = True
        field_print()


main()
if Game_Over == True:
    weiter = input(
        '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
    weiter = weiter.lower()
    while weiter != 'ja' and weiter != 'j' and weiter != 'y' and weiter != 'yes' and weiter != 'nein' and weiter != 'n' and weiter != 'no':
        print('\033[91m' + "[!] Bitte gib eine gültige Antwort ein! (Gültige Antworten: 'j', 'ja', 'y', 'yes', 'n', 'nein', 'no')" + '\033[0m')
        weiter = input(
            '\033[93m' + f'[?] Gratulation! Du hast ein Feld auf die erforderliche Punktzahl von {WIN_NUM} gebracht.\nWillst du im unbegrenzten Modus weiterspielen? (j/n)\n' + '\033[0m')
        weiter = weiter.lower()

    if weiter == 'ja' or weiter == 'j' or weiter == 'y' or weiter == 'yes':
        ok = 1
        daten['ok'] = ok
        with open(dateiname, 'w') as f:
            json.dump(daten, f)
        main()
    elif weiter == 'nein' or weiter == 'n' or weiter == 'no':
        Game_Over = True
        print('\033[94m' + "\n[!] Danke für's Spielen von Numtrip.\n-GPTDSM\n" + '\033[0m')
# TDSM
# ANSI Code '\033[X;XXm' for Color: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
