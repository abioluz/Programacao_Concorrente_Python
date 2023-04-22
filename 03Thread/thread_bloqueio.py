import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))
    lock = th.Lock() # para uma thread
    lock = th.RLock() # Para multiplas threads, pois evita que lock.acquire bloqueie
                      # se for chamada mais de uma vez

    # Lock
    lock.acquire()
    # Realiza qualquer operação com o recurso bloqueado para outras threads...
    try:
        pass
        # operação tratada
    except:
        pass
        # tratar a exceção...
    finally:
        # Unlock - Para desbloquear o processo e evitar o travameto de programa
        lock.release()


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))
    lock = th.Lock()

    with lock:
        pass
        # Realiza qualquer operação com o recurso bloqueado para outras threads



def contar(o_que, numero):
    for i in range (1, numero+1):
        print(f'{i}, {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    pass