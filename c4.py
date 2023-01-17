"""
Ćwiczenie:

Napisać program, który:

1. Wczytuje z pliku tekstowego dane:
 - nazwa towaru
 - ilość towaru
 - jednostka miary
 - cena

Plik jest w formacie:
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3


2. Po każdym towarze program dodaje dane do słownika zakupów w formacie:
{
'chleb': (3, 'szt', 4.6),
'cebula': (1.55, 'kg', 2.5)
}

3. Jeżeli towar już raz wystąpił i jest w słowniku to zamiast dodawać go
   drugi raz - zwiększamy ilość.

3. Używając danych ze słownika stowrzonego w pkt 2 wypisuje na ekran paragon w formie:
Pietruszka  2.0 kg x 4.60     9.20
Banany      3.0 kg x  3.5    10.50
----------------------------------
SUMA:                        19.70

Kolumny mają mieć szerokości:
nazwa - 12 znaków,
ilość - 2 znaki przed przecinkiem i 2 po
jednostka miary - 4 znaki
cena - 3 znaki przed przecinkiem i 2 po
wartość pozycji - 5 znaków przed i 2 po
SUMA - 7 znaków przed i 2 po

Podpowiedzi:
 - formatowanie f-stringow

 Rozszerzenia ćwiczenia:
 - co by było gdyby mógł wystąpić towar o różnych jednostkach miary.

"""
import json
import random
from pprint import pprint

DOMYSLNE_TOWARY = ('ser', 'mleko', 'piwo', 'kiwi', 'czipsy', 'makaron')
DOMYSLNE_JM = ('szt')


def parsuj_zakupy(nazwa_pliku='towary.txt'):
    slownik_rekordow = {}
    with open(nazwa_pliku, 'rt', encoding='utf8') as f:
        for linia in f:
            if linia.strip():
                nazwa, ilosc, jm, cena = linia.split()
                ilosc, cena = float(ilosc), float(cena)
                stara_ilosc = 0
                if nazwa in slownik_rekordow:
                    stara_ilosc = slownik_rekordow[nazwa][0]
                slownik_rekordow[nazwa] = [ilosc + stara_ilosc, jm, cena]
    return slownik_rekordow


def generuj_paragon(slownik_rekordow):
    suma = 0
    paragon = ''
    for nazwa, (ilosc, jm, cena) in slownik_rekordow.items():
        wartosc = ilosc * cena
        suma += wartosc
        paragon += f'{nazwa:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n'
    paragon += '-' * 41 + '\n'
    paragon += f'SUMA: {suma:35.2f}\n'
    return paragon


def _generuj_zakupy(ile_towarow, lista_towarow=DOMYSLNE_TOWARY):
    plik = ''
    d = {}
    for i in range(ile_towarow):
        towar = random.choice(lista_towarow)
        ilosc = float(random.randint(1, 10))
        jm = 'szt'
        cena = d[towar][-1] if towar in d else round(random.randint(1, 1000) / 100, 2)
        plik += f'{towar} {ilosc} szt {cena}\n'
        do_tej_pory = d[towar][0] if towar in d else 0
        d[towar] = [ilosc + do_tej_pory, jm, cena]
    return plik, d, generuj_paragon(d)


def _generuj_pliki(n=10):
    for i in range(n):
        with open(f'c4/in_{i}.txt', 'wt', encoding='utf8') as f_in, \
                open(f'c4/out_{i}.txt', 'wt', encoding='utf8') as f_paragon, \
                open(f'c4/out_{i}.json', 'wt', encoding='utf8') as f_dict:
            wejscie, d, paragon = _generuj_zakupy(random.randint(5, 15))
            f_in.write(wejscie)
            json.dump(d, f_dict)
            f_paragon.write(paragon)


if __name__ == '__main__':
    slownik_t = parsuj_zakupy()
    paragon = generuj_paragon(slownik_t)
    print(paragon)
