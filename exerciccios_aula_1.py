'primeira questão'
print('hello,world!')

'questão dois'
idade = int(input('quantos anos você tem ?'))

if idade >= 18:
    print('você ta meio velho irmão')

'questão tres '
expressao = input("dugite uma operação exemplo: 4 * 5 + 3")
resultado = eval(expressao)
print(f"o resultado da {expressao} é : {resultado}")


'questão dez'
from random import randint
numero = randint(1,10)
while True:
    usuario = int(input('fale um numero de 0 a 10'))
    if numero == usuario:
        print(f"o numero deu {numero} voce acertou")
        break
    elif numero > usuario:
        print(f"o numero deu{numero}grande de mais")
    else:
        print(f"o seu numero deu {numero}pequeno demais")



'questão quatro'


def compara_numero(a, b):
    if a > b:
        return f"{a} e maior que {b}"
    elif a < b:
        return f"{a} e menor que {b}"
    else:
        return f"{a} e igual a {b}"


numero1 = float(input('digite o primeiro numero:'))
numero2 = float(input('digite o segundo numero:'))

res = compara_numero(numero1, numero2)
print = (res)





'questão cinco'


def verificar_par(numero):
    if numero % 2 == 0:
        print(f"numero {numero} e par")
    elif numero % 2 == 1:  # if e elif precisam de condição (Ex: numero % 2 == 0:), else não precisa de condição
        print(f"numero {numero} e impar")

'questão seis'

'questão  sete'
for mensagem in range (0,101,2,):
    print(mensagem)