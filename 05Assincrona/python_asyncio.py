import asyncio

from utils.contador_decorator import contador

import math
import multiprocessing

from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

import asyncio

def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

async def aiocomputar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

@contador
def funccao_padrao(numero):
    computar(fim=numero)


@contador
def funcao_threads_proc(numero, qtd_cores):
    with ThreadPoolExecutor(max_workers=qtd_cores) as executor:
        funcao_interna(numero, qtd_cores, executor)

@contador
def funcao_processo(numero, qtd_cores):
    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        funcao_interna(numero, qtd_cores, executor)


def funcao_interna(numero, qtd_cores, executor):
    for n in range(1, qtd_cores + 1):
        ini = numero * (n - 1) / qtd_cores
        fim = numero * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        executor.submit(computar, inicio=ini, fim=fim)

@contador
def funcao_asyncio(numero, qtd_cores):
    el = asyncio.get_event_loop_policy().get_event_loop()
    lista=[]
    for n in range(1, qtd_cores + 1):
        ini = numero * (n - 1) / qtd_cores
        fim = numero * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')
        lista.append(el.create_task(aiocomputar(inicio=ini, fim=fim)))
    tarefas = asyncio.gather(*lista)
    el.run_until_complete(tarefas)
    el.close()

if __name__ == '__main__':
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).\n\n')
    mumero = 500_000_00
    print('função normal')
    funccao_padrao(mumero)
    print('\n\nCom thread')
    funcao_threads_proc(mumero, qtd_cores)
    print('\n\nCom Processo')
    funcao_processo(mumero, qtd_cores)
    print('\n\nCom Asyncio')
    funcao_asyncio(mumero, qtd_cores)
