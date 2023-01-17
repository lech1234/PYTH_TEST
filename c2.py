"""
Ćwiczenie:

Napisać program, który:
 1. Wczyta z konsoli kwotę brutto i stawkę VAT
 2. Wypisze kwotę netto i kwotę VAT wg podanej stawki

 Podpowiedzi:
 - input() zwraca zawsze obiekt str (napis) - konieczna jest konwersja do typów liczbowych

 Rozszerzenia ćwiczenia:
 - wczytać z konsoli i zamienić na liczbę w jednej linii

 Input:
 # 1230
 # 23
1230 / (1 + 23 / 100)
Output:
 # 1000
 # 230
"""
import sys

"""
Rozwiązanie:
"""


# Dodatkowe wymaganie
# -------------------
# stawka musi się mieścić w przedziale 0 <= stawka <= 100,
# jeżeli nie mieści to powinien wylecieć wyjątek ValueError z komunikatem "1233.0 - niepoprawna wartość stawki VAT"
# * kwota musi się mieścić w zakresie floata - jeżeli nie to też odpowiedni komunikat

def wylicz_netto(brutto, stawka):
    if not 0 <= stawka <= 100:
        raise ValueError(f'{stawka} - niepoprawna wartość stawki VAT')

    if not -sys.float_info.max <= brutto <= sys.float_info.max:
        raise ValueError(f'{brutto} - niepoprawna wartość kwoty brutto')

    netto = brutto / (1 + stawka / 100)
    vat = brutto - netto
    return netto, vat


if __name__ == '__main__':
    wylicz_netto(1230, -100)
    # brutto = float(input('Podaj kwotę brutto: '))
    # stawka = float(input('Podaj stawkę VAT: '))
    # netto, vat = wylicz_netto(brutto, stawka)
    # print('Brutto: ', brutto)
    # print('Netto: ', netto)
    # print('VAT: ', vat)
