from utils.contador_decorator import contador
import math
import threading
import multiprocessing

@contador
def funccao_padrao(numero):
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



# pegar o valor do processamento e não do preparo. Por mais que tudo junto já
# é mais rápido.


def funcao_thread2(numero, qtd_cores):
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
    rum(threads)

# Processo tentando por conta propria

# @contador
# def funcao_processo1(numero, qtd_cores): # este não deu certo
#     pool = multiprocessing.Pool(processes=qtd_cores)
#     for n in range(1, qtd_cores + 1):
#         ini = numero * (n - 1) / qtd_cores
#         fim = numero * n / qtd_cores
#         print(f'Core {n} processando de {ini} até {fim}')
#         pool.map(computar, (ini, fim),)
#     pool.close()
#     pool.join()

def funcao_processo2(numero, qtd_cores):
    processos = []
    for n in range(1, qtd_cores + 1):
        ini = numero * (n - 1) / qtd_cores
        fim = numero * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        processos.append(
            multiprocessing.Process(target=computar,
                             kwargs={'inicio': ini, 'fim': fim},
                             daemon=True)
        )
    rum(processos)


@contador
def rum(threads):
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
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).\n\n')
    mumero = 500_000_00
    # print('função normal')
    # funccao_padrao(mumero)
    # print('\n\nCom thread')
    # funcao_thread(mumero, qtd_cores)
    # # print('\n\nCom thread 2')
    # # funcao_thread2(mumero, qtd_cores)
    # print('\n\nCom Processo')
    # funcao_processo1(mumero, qtd_cores)
    funcao_processo2(mumero, qtd_cores)
   
