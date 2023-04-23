import multiprocessing
import ctypes

# Valor compartilhado do tipo int com valor defalt 0
contador = multiprocessing.Value('i')

# Valor compartilhado do tipo boolean com valor defalt False
ativo = multiprocessing.Value(ctypes.c_bool, False)

lock = multiprocessing.RLock()

# Valor compartilhado do tipo long, com valor default 0 e com o lock especificado
quantidade = multiprocessing.Value('I', 0, lock=lock)

# Array compartilhado do tipo int con os valores iniciais; 1, 2, 3, 4, 5
lista = multiprocessing.Array('i', [1, 2, 3, 4, 5])