from bubanj import Bubanj
from tiket import Tiket


tiket = Tiket()
bubanj = Bubanj()


def lucky_six():

    tiket.uplata_fn()
    bubanj.izvlacenje_brojeva()

    print(f'----------------------------------------------\nDobitak: {int(tiket.uplata) * bubanj.kvota} rsd\nKvota: {bubanj.kvota}\n'
          f'Broj pogodaka: {bubanj.pogoci}')


lucky_six()
