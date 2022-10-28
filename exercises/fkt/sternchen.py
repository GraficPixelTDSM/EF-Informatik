x = int(input("Wie hoch soll die Figur werden? "))
y = int(input("Wie breit soll die Figur werden? "))


def horizontal(breite):
    print("*" * breite)


def vertikal(höhe):
    for i in range(höhe - 2):
        print("*" + " " * (y - 2) + "*")


horizontal(y)
vertikal(x)
horizontal(y)
