import random
import time
from tiket import Tiket


class Bubanj:
    def __init__(self):
        self.tiket = Tiket()
        self.tiket.kombinacija_fn()       #unos kombinacije
        self.tiket.uplata_fn()
        self.brojevi = [i for i in range(1, 49)]    #lista brojeva za izvlacenje
        self.izvuceni_brojevi = []
        self.kombinacija_prikaz = self.tiket.kombinacija    #kombinacija u kojoj se izvuceni broj stavlja u zagrde
        self.kombinacija = [list(i) for i in self.kombinacija_prikaz] #za uporedjivanje sa listom izvucenih brojeva
        self.broj_kombinacija = len(self.kombinacija)
        self.prikaz = [i for i in range(1, 49)] #prikaz svih brojeva, i oznacavanje izvucenih
        self.kvote = [10000, 7500, 5000, 2500, 1000, 500, 300, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15,
                      10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.kvota = list()   #kvota na kojoj su pogodjeni svi brojevi u kombinaciji
        self.kvota_prikaz = '/'  #aktuelna kvota
        self.dobitne_kombinacije = []

    def izvlacenje_brojeva(self):
        for i in range(35):

            izvuceni_broj = random.choice(self.brojevi)
            self.brojevi.remove(izvuceni_broj)
            idx_izvucenog_broja = self.prikaz.index(izvuceni_broj)
            # noinspection PyTypeChecker
            self.prikaz[idx_izvucenog_broja] = '(' + str(izvuceni_broj) + ')'  #oznacavanje izvucenog broja
            self.izvuceni_brojevi.append(izvuceni_broj)

            if i > 4:
                self.kvota_prikaz = self.kvote[i - 5]

            print('Kombinacije:')
            for komb in self.kombinacija_prikaz:
                print(komb)
            print(f'Izvuceni broj: {izvuceni_broj}')
            print(f'Trenutna kvota: {self.kvota_prikaz}')
            print(f'Uplata po kombinaciji: {self.tiket.uplata}')
            print(self.prikaz)

            time.sleep(4)  # !!! za brzi rezultat, staviti 0
            if i != 34:
                print('\n' * 10)
            #ozncavanje izvucenog broje u kombinaciji
            for p in range(self.broj_kombinacija):
                for number in self.kombinacija[p]:
                    if number in self.izvuceni_brojevi:
                        idx = self.kombinacija[p].index(number)
                        self.kombinacija_prikaz[p][idx] = '(' + str(number) + ')'

            #dodela kvote
            for q in range(self.broj_kombinacija):
                pogoci = 0
                for number in self.kombinacija[q]:
                    if number in self.izvuceni_brojevi:
                        pogoci += 1
                        if pogoci == 6:
                            self.kvota.append(self.kvote[i - 5])
                            self.dobitne_kombinacije.append(self.kombinacija[q])

            #sprecavanje out of range greske
            for kom in self.dobitne_kombinacije:
                if kom in self.kombinacija:
                    self.kombinacija.remove(kom)
                    self.broj_kombinacija = len(self.kombinacija)
