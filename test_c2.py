import pytest

import c2

zero_stawka = [[(i * 100, 0), (i * 100, 0)] for i in range(10)]

dane = [
    ((1230, 23), (1000, 230)),
    ((1230., 23), (1000, 230)),
    ((1230, 23.), (1000, 230)),
    ((1230., 23.), (1000, 230)),
    ((0, 23), (0, 0)),
    ((123, 0), (123, 0)),
    *zero_stawka,
]

@pytest.fixture
def pusty_fixture():
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    return 55

@pytest.fixture
def dane_fixture(pusty_fixture):
    return dane


def test_simple_ok():
    assert c2.wylicz_netto(1230, 23) == pytest.approx((1000, 230)), 'Powinno wyjść 1000, 230'
    assert c2.wylicz_netto(1230., 23) == pytest.approx((1000, 230)), 'Powinno wyjść 1000, 230'
    assert c2.wylicz_netto(1230, 23.) == pytest.approx((1000, 230)), 'Powinno wyjść 1000, 230'
    assert c2.wylicz_netto(1230., 23.) == pytest.approx((1000, 230)), 'Powinno wyjść 1000, 230'


@pytest.mark.parametrize('t_in, t_out', dane)
def test_parametrized(t_in, t_out):
    assert c2.wylicz_netto(*t_in) == pytest.approx(t_out)


def test_dane_fixture(dane_fixture):
    for (kwota, stawka), wynik in dane_fixture:
        assert c2.wylicz_netto(kwota, stawka) == pytest.approx(wynik)


def test_bad_types():
    with pytest.raises(TypeError):
        c2.wylicz_netto('1230', '23')
    with pytest.raises(TypeError):
        c2.wylicz_netto('1230', 23)
    with pytest.raises(TypeError):
        c2.wylicz_netto(1230, '23')
    with pytest.raises(ValueError):
        c2.wylicz_netto(1234, -100)
    with pytest.raises(ValueError):
        c2.wylicz_netto(999 ** 999, -100)


def test_stawka_zakres():
    komunikat = r'\S+ - niepoprawna wartość stawki VAT'
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, 120)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, 101)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, 102)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, -1)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, -2)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(12, -18777)


def test_kwota_zakres():
    komunikat = r'\S+ - niepoprawna wartość kwoty brutto'
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(-999 ** 999, 20)
    with pytest.raises(ValueError, match=komunikat):
        c2.wylicz_netto(999 ** 999, 20)
