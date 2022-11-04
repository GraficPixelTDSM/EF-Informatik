y = int(input("Wie hoch soll die Figur werden? "))
x = int(input("Wie breit soll die Figur werden? "))


def horizontal(breite):
    print("*" * breite)


def vertikal(höhe):
    for i in range(höhe - 2):
        print("*" + " " * (x - 2) + "*")


def rechteck(x, y):
    horizontal(x)
    vertikal(y)
    horizontal(x)


rechteck(x, y)
