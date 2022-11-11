from time import *
prim = []


def main():
    print('''HINWEIS: Die Primzahlen von 1 bis 100'000, mit diesem Code zu berechnen dauert ca. 1079 Sekunden (17:59.147),
die Primzahlen von 1 bis 10'000 jedoch brauchen lediglich ca. 11 Sekunden (00:11.274).'''
          )
    N = int(input('Die Primzahlen von 1 bis wieviel willst du berechnet haben? '))
    start_time = time()
    for i in range(1, N + 1):  # erzeugt eine iterierbare Liste von 1 bis und mit N
        zähler = 0
        for w in range(1, N + 1):  # erzeugt eine iterierbare Liste von 1 bis und mit N
            x = i % w
            if x != 0:
                zähler = zähler + 1
        if zähler == (N - 2):
            print(i, " - ", round((i / N) * 100, 2), "%")
            prim.append(i)
    end_time = time()
    process_time = round((end_time - start_time), 3)
    print(f'Die Primzahlen von 1 bis {N} sind:')
    print(prim)
    print(f'Die oberen Zahlen sind die Primzahlen von 1 bis {N}. Die Berechnung hat {process_time} Sekunden gebraucht.')


main()
