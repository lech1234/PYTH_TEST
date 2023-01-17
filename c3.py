"""
Ćwiczenie:

 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Policzyć pole takiego trójkąta ze wzoru Herona
 3. Wypisać wynik na ekran

 Podpowiedzi:
 - Podniesienie do potęgi 1/2 to to samo co pierwiastkowanie - 4 ** 0.5 == 2
 - zawsze musimy stosować operatory - wyrażenie 3(4+7) jest niepoprawne, musi być 3*(4+7)
 - typ obiektu możemy sprawdzić za pomocą type(), np dla zmiennej x i typu str: if type(x) == str

 Rozszerzenia ćwiczenia:
 - jak stwierdzić, że trójąta o podanych bokach nie da się zbudować?
 - alternatywnie użyć math.sqrt

"""

"""
Rozwiązanie:
"""


def wylicz_pole(a, b, c):
    p = 0.5 * (a + b + c)
    x = p * (p - a) * (p - b) * (p - c)
    if x < 0:
        print('Nie ma takiego trójkąta')
    else:
        s = x ** 0.5
        return s


if __name__ == '__main__':
    a = float(input('Podaj długość boku: '))
    b = float(input('Podaj długość boku: '))
    c = float(input('Podaj długość boku: '))
    print(wylicz_pole(a, b, c))
    
    # 1. Tak po prostu
    # a, b, c = sorted([a, b, c])
    # if a + b > c:
    #     p = 0.5 * (a + b + c)
    #     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    #     print(s)
    # else:
    #     print('Nie ma takiego trójkąta')

    # 2. math.sqrt
    # p = 0.5 * (a + b + c)
    # try:
    #     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    #     print(s)
    # except ValueError:
    #     print('Nie ma takiego trójkąta')

    # 3. Sprawdzić typ wyniku
    # p = 0.5 * (a + b + c)
    # s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    # if type(s) is complex:
    #     print('Nie ma takiego trójkąta')
    # else:
    #     print(s)

    # sprawdzić to co jest pod pierwiastkiem:
    # p = 0.5 * (a + b + c)
    # x = p * (p - a) * (p - b) * (p - c)
    # if x < 0:
    #     print('Nie ma takiego trójkąta')
    # else:
    #     s = x ** 0.5
    #     print(s)
