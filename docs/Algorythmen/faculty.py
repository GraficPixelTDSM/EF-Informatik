x = 5


def fact(n):
    if n == 0:  # n == 0 statt n == 1, sodass bei fact(0) kein Fehler passiert
        return 1
    else:
        return n * fact(n - 1)


# Rekursiv (wie merge_sort)

print(fact(x))


def factS(n):
    if n == 0:
        return 1
    fac = n
    for i in range(1, n):
        fac = fac * i
    return fac


print(factS(x))
