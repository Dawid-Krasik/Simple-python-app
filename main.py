# Zadanie Mnożenie lab 7-8
# Author Dawid Krasik
# 

def konwersja(sliczba, dlugosc):
    liczba = [0 for i in range(dlugosc)]
    dl_sliczba = len(sliczba)
    for i in range(dl_sliczba):
        liczba[dlugosc - i - 1] = int(sliczba[dl_sliczba - i - 1])
    return liczba


def usun_minus(sliczba):
    if sliczba[0] == '-':
        sliczba = sliczba[1:]
    return sliczba


def czy_minus(d1, d2):
    if (d1[0] != d2[0]) and (d1[0] or d2[0] == '-'):
        print("-", sep='')


def pomnoz2(d1, d2):
    czy_minus = (d1[0] != d2[0]) and (d1[0] == '-' or d2[0] == '-')
    d1 = usun_minus(d1)
    d2 = usun_minus(d2)
    A = konwersja(d1, len(d1))
    B = konwersja(d2, len(d2))
    print(str(A), str(B), sep="\n")
    W = [0 for i in range(len(d1) + len(d2))]
    for i in range(len(d2) - 1, -1, -1):
        for j in range(len(d1) - 1, -1, -1):
            temp = B[i] * A[j]
            W[i + j] += temp
    if W[len(W) - 1] == 0:
        del W[len(W) - 1]
    Wk = [0 for i in range(len(W) + 1)]
    for i in range(- 1, -1 - len(W), -1):
        Wk[i] += W[i] % 10
        if i == -len(W):
            Wk[i] = W[i] % 10
            Wk[i - 1] = W[i] // 10
            break
        W[i - 1] += W[i] // 10
    if Wk[0] == 0:
        del Wk[0]

    if czy_minus:
        print("-", Wk)
    else:
        print(Wk)


dana1 = '-1523'
dana2 = '-553'

print("Wynik to: ")
pomnoz2(dana1, dana2)
