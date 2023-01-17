import json
import pytest
from c4 import generuj_paragon, parsuj_zakupy
import logging

LOGGER = logging.getLogger(__name__)

test_1_input = [
    ('ser 1 szt 20\n', {'ser': [1.0, 'szt', 20.0]}),
    ('ser 1 szt 20\nser 2 szt 20\n', {'ser': [3.0, 'szt', 20.0]}),
    ('ser 1 szt 20\nkawa 2 szt 10\n', {'ser': [1.0, 'szt', 20.0], 'kawa': [2., 'szt', 10.]}),
]


@pytest.mark.parametrize('t_input, t_expected', test_1_input)
def test_parsuj_zakupy_ok(tmp_path, t_input, t_expected):
    p = tmp_path / "tmp.txt"
    p.write_text(t_input)
    out = parsuj_zakupy(p)
    assert t_expected == out


def test_parsuj_files():
    i = 0
    while True:
        try:
            with open(f'c4/out_{i}.json', 'rt', encoding='utf8') as f_out_json, \
                    open(f'c4/out_{i}.txt', 'rt', encoding='utf8') as f_out_txt:
                d_expected = json.load(f_out_json)
                d = parsuj_zakupy(f'c4/in_{i}.txt')
                assert d_expected == d
                LOGGER.warning('---- Comparing dict expected:')
                LOGGER.warning(f'{d_expected}')
                LOGGER.warning('---- Got:')
                LOGGER.warning(f'{d}')
                paragon_expected = f_out_txt.read()
                paragon = generuj_paragon(d)
                LOGGER.warning('---- Comparing paragon expected:')
                LOGGER.warning(f'{paragon_expected}')
                LOGGER.warning('---- Got:')
                LOGGER.warning(f'{paragon}')
                assert paragon_expected == paragon
        except FileNotFoundError:
            break
        i += 1
