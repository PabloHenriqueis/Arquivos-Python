
def verificar_par(numero):
    if numero % 2 == 0:
        print(f"numero {numero} e par")
    elif numero % 2 == 1:  # if e elif precisam de condição (Ex: numero % 2 == 0:), else não precisa de condição
        print(f"numero {numero} e impar")


def media_lista(lista):
    return sum(lista)/len(lista) #lenght
