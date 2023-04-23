# Conceito de abstração trocando a importação

# from threading import Thread as Executar
from multiprocessing import Process as Executar
import time

def processar():
    print('[', end='', flush=True)
    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

if __name__ == '__main__':
    ex = Executar(target=processar)
    ex.start()
    ex.join()