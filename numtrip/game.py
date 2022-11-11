from random import randint
from colorama import init
from math import *
MAX_POTENZ = 5
col = 0
spiel = [[(2**(randint(1, MAX_POTENZ + 1))) for i in range(5)] for i in range(5)]
anzeige = [[], [], [], [], []]
print(spiel)
print('\033[93m' + 'Willkommen zu Numtrip! Klicke auf eine Zahl um alle anliegenden, gleichen Zahlen auf diesen Block zusammenzufassen.\nDabei wird der Wert der angeklickten Zahl verdoppelt. Es werden ständig neue Zahlen kommen, sobald du einige zusammenfasst. \nVersuche eine höchstmögliche Zahl zu erreichen!' +
      '\033[39m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')
for i in range(5):
    for j in range(5):
        if spiel[i][j] < 10:
            anzeige[i].append(f"  {spiel[i][j]} ")
        elif spiel[i][j] < 100:
            anzeige[i].append(f" {spiel[i][j]} ")
        elif spiel[i][j] < 1000:
            anzeige[i].append(f"{spiel[i][j]} ")
        else:
            anzeige[i].append(f"{spiel[i][j]}")
print('\033[35m' + '    01     02     03     04     05   ' + '\033[39m')
print(' ╔══════╤══════╤══════╤══════╤══════╗')
for i in range(5):
    def logg(pn):
        pn = int(log(int(anzeige[i][(pn - 1)])) / log(2) + 90)
        return pn
    print(" ║      │      │      │      │      ║")
    print('\033[35m' + str(i + 1) + '\033[39m' + "║", f'\033[1;{logg(1)}m' + anzeige[i][0], '\033[0;39m' + "│", f'\033[1;{logg(2)}m' + anzeige[i][1], '\033[0;39m' + "│", f'\033[1;{logg(3)}m' +
          anzeige[i][2], '\033[0;39m' + "│", f'\033[1;{logg(4)}m' + anzeige[i][3], '\033[0;39m' + "│", f'\033[1;{logg(5)}m' + anzeige[i][4], '\033[0;39m' + "║")
    print(" ║      │      │      │      │      ║")
    if i < 4:
        print(" ╟──────┼──────┼──────┼──────┼──────╢")
print(" ╚══════╧══════╧══════╧══════╧══════╝")

# log(zahl) / log(exponent)
# TDSM
# ANSI Code '\033[X;XXm' for Color: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
