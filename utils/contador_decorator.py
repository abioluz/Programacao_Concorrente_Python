import datetime

def contador(funcao):
    def funcao_decorada(*args, **kwargs):
        print(f'Inicio processamento.')
        inicio = datetime.datetime.now()
        funcao(*args, **kwargs)
        tempo = datetime.datetime.now() - inicio
        print(f'Terminou em {tempo.total_seconds():.2f} segundos.')
    return funcao_decorada