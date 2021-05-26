import random


class Tiket:

    def __init__(self):
        self.uplata = 0
        self.kombinacija = list()
        self.brojevi = [i for i in range(1, 49)]

    def uplata_fn(self):
        iznos = input('(RSD) Unesite iznos: ')
        try:
            if int(iznos) < 20:
                print('Minimalna uplata je 20 RSD\nPokusajte ponovo!')
                self.uplata_fn()
            else:
                self.uplata = int(iznos)
        except ValueError:
            print('Pogresan unos! Unesite samo cifre!')
            self.uplata_fn()

    def kombinacija_fn(self):
        upit = input('Zelite li automatsku kombinaciju? (Da/Ne): ').lower()

        if upit == 'da':
            self.kombinacija = sorted(random.sample(self.brojevi, 6))

        elif upit == 'ne':
            try:
                unos = input('Unesite svoje brojeve od 1 do 48 (bez zareza eg. 1 10 20): ')
                unos = unos.split()
                self.kombinacija = [int(i) for i in unos if int(i) < 49]

                if len(self.kombinacija) != 6:
                    print('Neophodno je uneti 6 cifara (1-48)!\nPokusajte ponovo!')
                    self.kombinacija_fn()

            except ValueError:
                print('Unesite samo brojeve od 1 do 48!\nPokusajte ponovo!')
                self.kombinacija_fn()
        else:
            print('Pogresan unos! \nOdgovorite sa da ili ne!')
            self.kombinacija_fn()
