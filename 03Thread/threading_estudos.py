import threading

def alguma_funcao(param):
    print('Executa algo...')
    print(f'Usa o parâmetro recebido: {param}')
    return param * param

if __name__ == '__main__':

    # Criação da Trhead passando a função. Note no exemplo o uso do lambda que pode ser
    # um bela forma de adicinar funções no thread

    th = threading.Thread(target=alguma_funcao, args=(4,), name='a')
    retorno = []
    th = threading.Thread(target=lambda:retorno.append(alguma_funcao(42)))

    th.start() # executa função a thread enviado a função em um pool de thread
    th.join()  # Não segue o programa até a thread ser finalizada

    # print(retorno)