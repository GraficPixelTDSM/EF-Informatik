from random import randint
from colorama import init
from math import*
MAX_POTENZ = 5
col = 0
spiel = [[(2**(randint(1, MAX_POTENZ+1))) for i in range(5)] for i in range(5)]
anzeige = [[],[],[],[],[]] 
print(spiel)
for i in range(5):
    for j in range(5):
        if spiel[i][j] < 10:
            anzeige[i].append(f"  {spiel[i][j]} ")
        elif spiel[i][j] < 100:
            anzeige[i].append(f" {spiel[i][j]} ")
        elif spiel[i][j] < 1000:
            anzeige[i].append(f"{spiel[i][j]} ")
print('╔══════╤══════╤══════╤══════╤══════╗')
for i in range(5):
    p1 = int(log(int(anzeige[i][0])) / log(2) + 30)
    p2 = int(log(int(anzeige[i][1])) / log(2) + 30)
    p3 = int(log(int(anzeige[i][2])) / log(2) + 30)
    p4 = int(log(int(anzeige[i][3])) / log(2) + 30)
    p5 = int(log(int(anzeige[i][4])) / log(2) + 30)
    print("║      │      │      │      │      ║")
    print("║",f'\033[{p1}m' + anzeige[i][0], '\033[39m' + "│", f'\033[{p2}m' + anzeige[i][1],'\033[39m' + "│",f'\033[{p3}m' + anzeige[i][2],'\033[39m' + "│",f'\033[{p4}m' + anzeige[i][3],'\033[39m' + "│",f'\033[{p5}m' + anzeige[i][4],'\033[39m' + "║")
    print("║      │      │      │      │      ║")
    if i < 4:
        print("╟──────┼──────┼──────┼──────┼──────╢")
print("╚══════╧══════╧══════╧══════╧══════╝")

# log(zahl) / log(exponent)