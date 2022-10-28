from random import randint
import time
k = 0

while k != 11:
    x = randint(2, 30)
    y = randint(2, 30)

    def horizontal(breite):
        print("*" * breite)

    def vertikal(höhe):
        for i in range(höhe - 2):
            print("*" + " " * (y - 2) + "*")

    horizontal(y)
    vertikal(x)
    horizontal(y)
    k = k + 1
    time.sleep(1)
