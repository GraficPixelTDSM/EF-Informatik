from time import *
from math import *
prim = [2]


def main():
    print('''HINWEIS: Die Primzahlen von 1 bis 100'000, mit diesem Code zu berechnen dauert ca. 157.234 Sekunden (02:37.234),
die Primzahlen von 1 bis 10'000 jedoch brauchen lediglich ca. 2.209 Sekunden (00:02.209).'''
          )
    N = int(input('Die Primzahlen von 1 bis wieviel willst du berechnet haben? '))
    start_time = time()
    for i in range(1, N + 1):  
        zähler = 0
        for w in range(int(sqrt(i))):  
            x = i % prim[w]
            if x == 0:
                break
            if x != 0 and i != 1:
                zähler = zähler + 1
            
        if zähler == (int(sqrt(i))):
            print(i, " - ", round((i / N) * 100, 2), "%")
            prim.append(i)
    end_time = time()
    process_time = round((end_time - start_time), 3)
    print(f'Die Primzahlen von 1 bis {N} sind:')
    print(prim)
    print(f'Die oberen Zahlen sind die Primzahlen von 1 bis {N}. Die Berechnung hat {process_time} Sekunden für die Berechnung von {len(prim)} Primzahlen gebraucht.')


main()
