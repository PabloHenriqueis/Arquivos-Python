def saudacao():
    print('boa tarde')


def dia(diadasemana):
    print(f'hoje é {diadasemana}-feira')


def produto(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

saudacao()
resp = (input('qual o dia da semana é hoje (ex:terça ou quarta)'))
dia(resp)
print(produto(8, 2))

"variaveis compostas"

tupla = (1, 2, 5, 8, 3, 9, 4)
lista = [10, 20, 50, 40, 20]
dicionario = {
    'nome' : 'pablo',
    'idade': 800,
    'cidade' : 'gotam city'

}
tupa0rga = sorted(tupla) #organizar tupla=sorted
print(tupa0rga)
maximo = max(tupla)
minimo = min(tupla)
print(maximo)
print(minimo)

#oerganizar lista =  liestaOrganizada = lista.sort()

liestaOrganizada = lista.sort()
maxlista = max(lista)
print(lista)
lista.append(80) # append ultima posição
lista.insert(0,50)  # inset onde desejar de acordo com o indicie
print(lista)
lista.remove(40) # usa o valor da lista
lista.pop(0) # usa o indicie da lista
'''
print(dicionario.keys()) # chaves
print(dicionario.values()) #valores
print(dicionario.items()) #itens
'''
def conversao(tupla):
    return ''.join(tupla)

letras = conversao(('p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'c', 'a', 'o'))
resultado = conversao(letras)
print(resultado.upper()) #lower minuscula // upper maiscula

