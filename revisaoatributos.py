class Aluno:
    def __init__(self , nome , idade ,  sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


    def apresentacao(self):
        return print(f'me chamo {self.nome}, tenho {self.idade}'
                     f'anos de idade e sou do sexo {self.sexo}')


class Escola:
    def __init__(self , nome ):
        self.nome = nome
        self.alunos = []

    def adicionar_alunos(self , aluno):
        self.alunos.append(aluno)


aluno1 = Aluno('jackt', '20' , 'masculino')
aluno2 = Aluno('ferr' , '23' , ' feminino')

escola =  Escola('Polo icp')
escola.adicionar_alunos(aluno1)
escola.adicionar_alunos(aluno2)

print(escola.alunos[1].apresentacao())
print(escola.nome)