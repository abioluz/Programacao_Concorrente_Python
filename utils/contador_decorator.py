import datetime
import multiprocessing
def contador(funcao):
    def funcao_decorada(*args, **kwargs):
        qtd_cores = multiprocessing.cpu_count()
        print(f'Realizando o processamento matemático com {qtd_cores} core(s).')
        inicio = datetime.datetime.now()
        funcao(*args, **kwargs, qtd_cores=qtd_cores)
        tempo = datetime.datetime.now() - inicio
        print(f'Terminou em {tempo.total_seconds():.2f} segundos.')
    return funcao_decorada