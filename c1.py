import random
import json

import faker


# otworzyć plik:
def wyciagnij_imie_kwote(line):
    imie, kwota = line.split()
    kwota = float(kwota)
    return imie, kwota


def parsuj_zobowiazania(nazwa_pliku='zobowiazania.txt'):
    with open(nazwa_pliku, 'rt', encoding='utf8') as f:
        dlugi = {}
        for line in f:
            line = line.lower().strip()
            if line:
                try:
                    imie, kwota = wyciagnij_imie_kwote(line)
                except ValueError:
                    continue
                dlugi[imie] = round(dlugi.get(imie, 0) + kwota, 3)
    return dlugi


def main():
    dlugi = parsuj_zobowiazania()
    for imie, kwota in dlugi.items():
        print(f'{imie.capitalize():10} wisi mi {kwota:6.2f} zł.')


def generuj_pliki(plikow=10, wpisow=20, imion=10):
    fk = faker.Faker('PL_pl')
    with open(f'c1/in_0.txt', 'wt', encoding='utf8') as f, \
            open(f'c1/out_0.json', 'wt', encoding='utf8') as f_json:
        json.dump({}, f_json)

    for plik_no in range(1, plikow + 1):
        imiona = [fk.first_name().split()[0] for _ in range(imion)]
        with open(f'c1/in_{plik_no}.txt', 'wt', encoding='utf8') as f, \
                open(f'c1/out_{plik_no}.json', 'wt', encoding='utf8') as f_json:
            d = {}
            for _ in range(wpisow):
                imie = random.choice(imiona)
                kwota = random.randrange(0, 10_000_000) / 100
                if random.random() > 0.95:
                    f.write('\n')
                if random.random() > 0.95:
                    f.write(' \t  \n')
                if random.random() > 0.95:
                    f.write('        \n')
                if random.random() > 0.5:
                    imie = imie.lower()
                f.write(f'{imie} {kwota}\n')

                d[imie.lower()] = round(d.get(imie.lower(), 0) + kwota, 3)
            json.dump(d, f_json, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    generuj_pliki()
