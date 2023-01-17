import json

import pytest, faker
from c1 import wyciagnij_imie_kwote, parsuj_zobowiazania


def test_wyciagnij_imie_kwote_ok():
    f = faker.Faker('PL_pl')
    for _ in range(10):
        imie = f.first_name()
        for kwota in [0, 11, 111999, 12.775632, 1.33333333, -1, -12.6666666]:
            assert imie, kwota == wyciagnij_imie_kwote(f'{imie} f{kwota}')
            assert imie, kwota == wyciagnij_imie_kwote(f'{imie} f{kwota:e}')

def test_wyciagnij_imie_kwote_errors():
    with pytest.raises(ValueError, match='not enough'):
        imie, kwota = wyciagnij_imie_kwote('ala')
        imie, kwota = wyciagnij_imie_kwote('11.22')
    with pytest.raises(ValueError, match='too many'):
        imie, kwota = wyciagnij_imie_kwote('ala 12 22')
        imie, kwota = wyciagnij_imie_kwote('11.22 ala 444')

    with pytest.raises(ValueError, match='could not convert string to float'):
        imie, kwota = wyciagnij_imie_kwote('ala ola')
        imie, kwota = wyciagnij_imie_kwote('ala 11,33')
        imie, kwota = wyciagnij_imie_kwote('12 ala')
        imie, kwota = wyciagnij_imie_kwote('ala nan')
        imie, kwota = wyciagnij_imie_kwote('ala None')


def test_parsuj_files():
    i = 0
    while True:
        try:
            with open(f'c1/out_{i}.json', 'rt', encoding='utf8') as f_out:
                j1 = parsuj_zobowiazania(f'c1/in_{i}.txt')
                j2 = json.load(f_out)
                assert j1 == j2
        except FileNotFoundError:
            break
        i += 1