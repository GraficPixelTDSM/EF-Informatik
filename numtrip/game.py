from random import randint
from colorama import init
from math import *
MAX_POTENZ = 5
col = 0
spiel = [[(2**(randint(1, MAX_POTENZ + 1))) for i in range(5)] for i in range(5)]
anzeige = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
check = [[], []]
print(spiel)
print('\033[93m' + 'Willkommen zu Numtrip! Klicke auf eine Zahl um alle anliegenden, gleichen Zahlen auf diesen Block zusammenzufassen.\nDabei wird der Wert der angeklickten Zahl verdoppelt. Es werden ständig neue Zahlen kommen, sobald du einige zusammenfasst. \nVersuche eine höchstmögliche Zahl zu erreichen!' +
      '\033[39m' + '\n\n════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n')


for i in range(5):
    for j in range(5):
        if spiel[i][j] < 10:
            anzeige[i][j] = f"  {spiel[i][j]} "
        elif spiel[i][j] < 100:
            anzeige[i][j] = f" {spiel[i][j]} "
        elif spiel[i][j] < 1000:
            anzeige[i][j] = f"  {spiel[i][j]}"
        else:
            anzeige[i][j] = f"{spiel[i][j]}"
print('\033[35m' + '    01     02     03     04     05   ' + '\033[39m')
print(' ╔══════╤══════╤══════╤══════╤══════╗')
i = 0
for i in range(5):
    def logg(p):
        pn = int(log(int(spiel[i][(p - 1)])) / log(2) + 90)
        return pn
    print(" ║      │      │      │      │      ║")
    print('\033[35m' + str(i + 1) + '\033[39m' + "║", f'\033[1;{logg(1)}m' + anzeige[i][0], '\033[0;39m' + "│", f'\033[1;{logg(2)}m' + anzeige[i][1], '\033[0;39m' + "│", f'\033[1;{logg(3)}m' +
          anzeige[i][2], '\033[0;39m' + "│", f'\033[1;{logg(4)}m' + anzeige[i][3], '\033[0;39m' + "│", f'\033[1;{logg(5)}m' + anzeige[i][4], '\033[0;39m' + "║")
    print(" ║      │      │      │      │      ║")
    if i < 4:
        print(" ╟──────┼──────┼──────┼──────┼──────╢")
print(" ╚══════╧══════╧══════╧══════╧══════╝")


def check_num_input(inp):
    if inp.isnumeric():
        return True
    else:
        return False


def checkn():
    pass


x_a = input('Welche Position auf der X-Achse willst du auswählen? ')
y_a = input('Welche Position auf der Y-Achse willst du auswählen? ')
while check_num_input(x_a) is False:
    x_a = input('Welche Position auf der X-Achse willst du auswählen? ')
while check_num_input(y_a) is False:
    y_a = input('Welche Position auf der Y-Achse willst du auswählen? ')

# log(zahl) / log(exponent)
# TDSM
# ANSI Code '\033[X;XXm' for Color: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
