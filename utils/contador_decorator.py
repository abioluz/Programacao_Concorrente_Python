import datetime
def contador(funcao):
    def funcao_decorada(*args, **kwargs):
        global lista
        print('Iniciando...')
        inicio = datetime.datetime.now()
        funcao(*args, **kwargs)
        tempo = datetime.datetime.now() - inicio
        print(f'Terminou em {tempo.total_seconds():.2f} segundos.')
        lista.append(tempo.total_seconds())
    return funcao_decorada