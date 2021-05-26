from bubanj import Bubanj
from tiket import Tiket


bubanj = Bubanj()


def lucky_six():

    bubanj.izvlacenje_brojeva()

    dobitak = round(sum(bubanj.kvota) * bubanj.tiket.uplata, 2)

    print(f'----------------------------------------------\nKvota: {bubanj.kvota}\nDobitak: {dobitak}')


lucky_six()
