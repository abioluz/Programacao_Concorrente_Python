import multiprocessing
from utils.contador_decorator import contador
def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1

def sacar(saldo,lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1

def realizar_transacoes(saldo, lock):
    lista = [
    multiprocessing.Process(target=depositar, args=(saldo, lock)),
    multiprocessing.Process(target=sacar, args=(saldo, lock))
    ]

    [pc.start() for pc in lista]
    [pc.join() for pc in lista]

@contador
def main(saldo, lock):
    for _ in range(100):
        realizar_transacoes(saldo, lock)
    print(f'Saldo Final: {saldo.value}')


if __name__ == '__main__':
    lock = multiprocessing.RLock()
    saldo = multiprocessing.Value('i', 100)
    print(f'Saldo inicial: {saldo.value}')

    main(saldo, lock)