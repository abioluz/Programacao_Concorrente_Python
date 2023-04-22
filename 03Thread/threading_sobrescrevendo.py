import threading

class Thread(threading.Thread):
    '''
    Sobrescrevendo para poder obter o resultado da função
    '''
    def run(self):
        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

        """
        try:
            if self._target is not None:
                # self._target(*self._args, **self._kwargs)

                # GAMBIARRA simples para obter o resultado da thread
                self.result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs




def alguma_funcao(param):
    print('Executa algo...')
    print(f'Usa o parâmetro recebido: {param}')
    return param * param


if __name__ == '__main__':

    # Criação da Trhead passando a função. Note no exemplo o uso do lambda que pode ser
    # um bela forma de adicinar funções no thread

    th = Thread(target=alguma_funcao, args=(42,))

    th.start() # executa função a thread enviado a função em um pool de thread
    th.join()  # Não segue o programa até a thread ser finalizada

    print(f'Retorno da thread sobrescrita{th.result}')