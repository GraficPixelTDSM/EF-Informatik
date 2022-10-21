from random import randint
words = ['Affe', 'Elefant', 'Biber']

feld = [[' +----+\n', ' |\n', ' |\n', ' |\n', ' |\n', ' |\n', ' ________\n', '/        \n']]
losslvl = 0

def game():
    gword = words[randint(0, len(words) - 1)]
    print(gword)
    for i in range(len(feld[loss])):
        print(feld[0][i])


game()


def show():
    pass
