import asyncio
import datetime


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')
    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f'{quantidade} dados gerados com suscesso...')

async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde o processamento de {quantidade} dados...')
    processados = 0
    while processados< quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.001)
    print(f'Foram processados {processados} itens')

def main():
    total = 5_000
    dados = asyncio.Queue()
    print(f'Computando {total * 2:.2f} dados. ')
    # el = asyncio.get_event_loop()
    # não sei se assim seria adequando para pythom 3.10
    el = asyncio.get_event_loop_policy().get_event_loop()
    tarefa1 = el.create_task(gerar_dados(total, dados))
    tarefa2 = el.create_task(gerar_dados(total, dados))
    tarefa3 = el.create_task(processar_dados(total*2, dados))
    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)

    el.run_until_complete(tarefas)

def main2():
    total = 5_000
    dados = asyncio.Queue()
    print(f'Computando {total * 2:.2f} dados. ')

    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)
    # não sei se assim seria adequando para pythom 3.10

    tarefa1 = el.create_task(gerar_dados(total, dados))
    tarefa2 = el.create_task(gerar_dados(total, dados))
    tarefa3 = el.create_task(processar_dados(total*2, dados))
    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)

    el.run_until_complete(tarefas)


# Não é assim, mas vou ver certinho com a documentação
# async def main2():
#     total = 5_000
#     dados = asyncio.Queue()
#     print(f'Computando {total * 2:.2f} dados. ')
#     tarefa1 = asyncio.create_task(gerar_dados(total, dados))
#     tarefa2 = asyncio.create_task(gerar_dados(total, dados))
#     tarefa3 = asyncio.create_task(processar_dados(total*2, dados))
#     tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)
#
#     asyncio.run(tarefas)



if __name__ == '__main__':
    main2()
    print('FIM')


