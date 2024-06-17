#1 forma de  importar biblioteca (importar todas as bibliotecas)
import math

potencial = math.pow(3, 3)
print(math.pi)
print(potencial)
print(math.sqrt(144))

#2 forma de importar bibliotecas ()
from math import sqrt , floor , ceil
print(sqrt(225))
print(floor (2.62))
print(ceil(2.62))

#3 forma de importar biblioteca (renomear a biblioteca)
import math as M
print(M.pi)

#4 forma de importar bibliotecas (trazer as funções da biblioteca para seu código)
from math import *
print(pow(2,5))