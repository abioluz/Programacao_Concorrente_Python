import multiprocessing

def faz_algo(valor):
    print(f'Fazendo algo com {valor}')
    for i in range(1, 1+valor):
        valor = valor*valor
        print(i)
    return 'Finaliznado'

def main(valor):
    pc = multiprocessing.Process(target=faz_algo, args=(valor,))
    pc.start()
    pc.join()

if __name__ == '__main__':
    main(26)
    print('FIM')
