import multiprocessing
from utils.contador_decorator import contador
def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1

def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1


def realizar_transacoes(saldo):
    lista = [
    multiprocessing.Process(target=depositar, args=(saldo,)),
    multiprocessing.Process(target=sacar, args=(saldo,))
    ]

    [pc.start() for pc in lista]
    [pc.join() for pc in lista]

@contador
def main(saldo):
    for _ in range(100):
        realizar_transacoes(saldo)
    print(f'Saldo Final: {saldo.value}')

if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)
    print(f'Saldo inicial: {saldo.value}')

    main(saldo)