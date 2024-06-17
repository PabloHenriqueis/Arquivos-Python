"funcao de saudacao"
def saudacao():
    print('boa tarde')


def dia(nome):
    print(f'boa tarde {nome}')





saudacao()
"ano bisexto"


resp = (input('digite seu nome'))
dia(resp)


def eh_bissexto(ano):
    # Verifica se o ano é divisível por 4
    if ano % 4 == 0:
        # Se o ano for divisível por 100, ele também deve ser divisível por 400
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto e exibe a mensagem correspondente
if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


lista = [10, 20, 50, 40, 20]


liestaOrganizada = lista.sort()
maxlista = max(lista)
print(lista)
lista.append(80) # append ultima posição
lista.insert(0,50)  # inset onde desejar de acordo com o indicie
print(lista)
lista.remove(40) # usa o valor da lista
lista.pop(0) # usa o indicie da lista


nome = ('p', 'a', 'b', 'l', 'o')
print(nome)
listanova = ''.join(nome)
print(listanova)

naicimento = {
    'pablo': 2006,
    'nicole': 2009,
    'jacal': 1,
}

print(naicimento.items())

A = {1, 2, 3, 4 }
B = {4, 5, 6, 7, 8 }
C = {4, 5, 8, 9 }
uniao = A.union(B,C) #função de união de união
print(uniao)
intersecao = B.intersection(C) # função de interseção dos conjuntos
print(intersecao)