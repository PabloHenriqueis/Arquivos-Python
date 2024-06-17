class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return print(f'o aluno tem {self.nome} tem {self.idade} anos')


class Escola:
    def __init__(self, nome, bairro, andares):
        self.nome = nome
        self.bairro = bairro
        self.andares = andares
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


# programa principal

aluno1 = Aluno('sr.P', 20)
aluno2 = Aluno('ms.h', 23)
aluno3 = Aluno('sir.s', 34)

escola = Escola('credo', 'venesa', '7')
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
escola.adicionar_aluno(aluno3)
print(f'escola de ??? fica no bairro{escola.bairro} é tem {escola.andares}')
print(escola.alunos[0].apresentar())
