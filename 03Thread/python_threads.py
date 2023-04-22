from utils.contador_decorator import contador
import math
import threading


@contador
def funccao_padrao(numero, qtd_cores):
    computar(fim=numero)

@contador
def funcao_thread(numero, qtd_cores):
    threads = []
    for n in range(1, qtd_cores + 1):
        ini = numero * (n - 1) / qtd_cores
        fim = numero * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        threads.append(
            threading.Thread(target=computar,
                             kwargs={'inicio': ini, 'fim': fim},
                             daemon=True)
        )

    [th.start() for th in threads]
    [th.join() for th in threads]


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))
#
if __name__ == '__main__':
    mumero = 500_000_000
    print('função normal\n')
    funccao_padrao(mumero)
    print('\n\nCom thread\n')
    funcao_thread(mumero)

