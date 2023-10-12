import math
num = int(input('digite um numero: '))
print('A raiz de {} é {}'.format(num, math.sqrt(num)))

print('A raiz de {} aredondada pra cima é {}'.format(num,math.ceil( math.sqrt(num))))

print('A raiz de {} aredondada pra baixo é {}'.format(num,math.floor( math.sqrt(num))))

from math import sqrt, ceil, floor

num = int(input('digite um numero: '))
print('A raiz de {} é {}'.format(num, sqrt(num)))

print('A raiz de {} aredondada pra cima é {}'.format(num, ceil(sqrt(num))))

print('A raiz de {} aredondada pra baixo é {}'.format(num, floor(sqrt(num))))

import random

print(random.random())
print(random.randint(1, 10))

