import matplotlib.pyplot as plt

nomes = []
medias = []

def adicionar(nome, n1, n2):
    nomes.append(nome)
    media = (n1 + n2)/2
    medias.append(media)



def grafico():
    plt.bar(nomes,medias)
    plt.xlabel('media de alunos')
    plt.ylabel('media dos alunos')
    plt.title('histograma com media de alunos')
    plt.show()
