from random import randint
from colorama import init
from math import*
MAX_POTENZ = 6
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
        print(spiel[i][j])
print('╔══════╤══════╤══════╤══════╤══════╗')
for i in range(5):
    print("║      │      │      │      │      ║")
    print("║",anzeige[i][0],"│", anzeige[i][1],"│",anzeige[i][2],"│",anzeige[i][3],"│",anzeige[i][4],"║")
    print("║      │      │      │      │      ║")
    if i < 4:
        print("╟──────┼──────┼──────┼──────┼──────╢")
print("╚══════╧══════╧══════╧══════╧══════╝")
