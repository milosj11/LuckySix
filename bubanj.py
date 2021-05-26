import random
import time
from tiket import Tiket


class Bubanj:
    def __init__(self):
        self.tiket = Tiket()
        self.tiket.kombinacija_fn()       #unos kombinacije
        self.brojevi = [i for i in range(1, 49)]    #lista brojeva za izvlacenje
        self.izvuceni_brojevi = []
        self.kombinacija_prikaz = self.tiket.kombinacija    #kombinacija u kojoj se izvuceni broj stavlja u zagrde
        self.kombinacija = [i for i in self.kombinacija_prikaz] #za uporedjivanje sa listom izvucenih brojeva
        self.prikaz = [i for i in range(1, 49)] #prikaz svih brojeva, i oznacavanje izvucenih
        self.kvote = [10000, 7500, 5000, 2500, 1000, 500, 300, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15,
                      10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.kvota = 0   #kvota na kojoj su pogodjeni svi brojevi u kombinaciji
        self.kvota_prikaz = '/'  #aktuelna kvota

    def izvlacenje_brojeva(self):
        for i in range(35):
            if self.kvota == 0:
                self.pogoci = 0 #broj pogodaka se restartuje prilikom svake iteracije

            izvuceni_broj = random.choice(self.brojevi)
            self.brojevi.remove(izvuceni_broj)
            idx_izvucenog_broja = self.prikaz.index(izvuceni_broj)
            # noinspection PyTypeChecker
            self.prikaz[idx_izvucenog_broja] = '(' + str(izvuceni_broj) + ')'  #oznacavanje izvucenog broja
            self.izvuceni_brojevi.append(izvuceni_broj)

            if i > 4:
                self.kvota_prikaz = self.kvote[i - 5]

            print(f'Vasa kombinacija: {self.kombinacija_prikaz}')
            print(f'Izvuceni broj: {izvuceni_broj}')
            print(f'Trenutna kvota: {self.kvota_prikaz}')
            print(self.prikaz)

            time.sleep(3)
            if i != 34:
                print('\n' * 10)

            if self.kvota == 0:
                for broj in self.kombinacija: #proveravanje broja pogodaka
                    if broj in self.izvuceni_brojevi:
                        self.pogoci += 1
                        idx_u_kombinaciji = self.kombinacija.index(broj)
                        self.kombinacija_prikaz[idx_u_kombinaciji] = '(' + str(broj) + ')'

                if self.pogoci == 6: #dobitna kvota
                    self.kvota = self.kvote[i - 5]
