from typing import Generator
import time
def fibo() -> Generator[int, None, None]:
    valor: int = 0
    proximo: int = 1
    while True:
        valor, proximo = proximo, valor + proximo
        yield valor


if __name__ == '__main__':

    for n in fibo():
        print(n, end=', ', flush=True)
        if n > 100:
            break
        # time.sleep(1)
    print('\nPronto!')

