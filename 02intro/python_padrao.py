from utils.contador_decorator import contador
import math

@contador
def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))
#
if __name__ == '__main__':
    for i in range(10):
        computar(fim=50000000) # Terminou em 17.65 segundos.

