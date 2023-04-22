import threading
import random
import time

from typing import List
import colorama

lock = threading.RLock()

class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo

def main():
    contas = criar_contas()
    with lock:
        total = sum(conta.saldo for conta in contas)

    print('Iniciando Transferencias...')

    numero_thread = 30

    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)) for _ in range(numero_thread)
    ]
    [tarefa.start() for tarefa in tarefas]

    print('Transferencias completas.')
    valida_banco(contas, total)

def servicos(contas, total):
    for _ in range(1,10_000):
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)

def criar_contas() -> List[Conta]:
    return [Conta(saldo=random.randint(5_000, 10_000)) for _ in range(6)]

def transferir(origem: Conta, destino: Conta, valor: int):

    if origem.saldo < valor:
        return
    with lock:
        origem.saldo -= valor
        time.sleep(0.001)
        destino.saldo += valor

def valida_banco(contas: List[Conta], total: int):
    with lock:
        atual = sum(conta.saldo for conta in contas)

    if atual != total:
        print(colorama.Fore.RED + f'ERRO: Balanço bancário inconsistente. BRL$ {atual:.2f} vs {total:.2f}', flush=True)
    else:
        pass
        # print(colorama.Fore.GREEN + f'Tudo certo: Balanço bancário consistente: BRL$ {total:.2f}', flush=True)

def pega_duas_contas(contas):
    c1 = random.choice(contas)
    c2 = random.choice(contas)

    while c1 == c2:
        c2 = random.choice(contas)

    return c1, c2
if __name__ == '__main__':
    main()
    print("fim")