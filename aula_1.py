dia = 'segunda'
data = 3
print( 'hoje é {dia} dia {data}' )

NOME = str(input('qual o seu nome?'))
n1 = int (input('digite um valor'))
n2 = int (input('digite segundo valor'))
print(NOME)
print(n1 + n2 )
'''
+ - adição
- - subtração
/ - divisão
// - divisão interira
** - potencia
% - resto da divisão 

'''
idade = int(input('quantos anos você tem ?'))

if idade < 18:
    print('você não precisa se alistar com essa idade')
elif idade == 18:
    print('você precisa se alistar')
else:
    print('você passou da idade de se alistar')
print('volte sempre!')

'''

< -  menor 
> - maior 
<= - menor ou igual
>= - menor ou igual
== - igual
!= - diferente

'''
for mensagem in range (10,-1,-1,):
    print(mensagem)