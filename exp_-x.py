# Aproxima o valor de exp(-x) usando n dígitos significativos.
# github: rsdavid35

from sigfig import round
from functools import reduce
import math, warnings
warnings.filterwarnings("ignore")

x = float(input('x: '))
n_termos = int(input('número de termos: '))
sig = int(input('digitos significativos: '))

# lista de termos
nums = []

# k variando de 0 a n_termos.
for k in range(0, n_termos + 1):
    # avalia a função para o valor de k
    num = ((-1)**k) * (x)**k / math.factorial(k)
    # considera sig dígitos significativos, com arredondamento, e adiciona a lista de termos.
    nums.append(round(num, sigfigs = sig))

# soma todos os termos da lista.
soma = round(reduce(lambda x, y: x + y, nums), sigfigs= sig)

print('termos:', nums, '\nexp(-'+str(x)+')=', soma)

input('pressione alguma tecla para sair...')
