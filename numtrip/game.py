from random import randint
from colorama import init
from math import *
MAX_POTENZ = 5
col = 0
spiel = [[(2**(randint(1, MAX_POTENZ + 1))) for i in range(5)] for i in range(5)]
anzeige = [[], [], [], [], []]
print(spiel)
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
print('╔══════╤══════╤══════╤══════╤══════╗')
for i in range(5):
    def logg(pn):
        pn = int(log(int(anzeige[i][(pn - 1)])) / log(2) + 30)
        return pn
    print("║      │      │      │      │      ║")
    print("║", f'\033[{logg(1)}m' + anzeige[i][0], '\033[39m' + "│", f'\033[{logg(2)}m' + anzeige[i][1], '\033[39m' + "│", f'\033[{logg(3)}m' +
          anzeige[i][2], '\033[39m' + "│", f'\033[{logg(4)}m' + anzeige[i][3], '\033[39m' + "│", f'\033[{logg(5)}m' + anzeige[i][4], '\033[39m' + "║")
    print("║      │      │      │      │      ║")
    if i < 4:
        print("╟──────┼──────┼──────┼──────┼──────╢")
print("╚══════╧══════╧══════╧══════╧══════╝")

# log(zahl) / log(exponent)
