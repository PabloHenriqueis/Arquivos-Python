
class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class SistemaDeProfessores:
    def __init__(self):
        self.professores = []

    def adicionar_professor(self, nome, disciplina):
        novo_professor = Professor(nome, disciplina)
        self.professores.append(novo_professor)
        print(f"Professor {nome} adicionado com sucesso!")

    def listar_professores(self):
        print("Lista de Professores:")
        for professor in self.professores:
            print(f"Nome: {professor.nome}, Disciplina: {professor.disciplina}")


# Exemplo de uso:
sistema = SistemaDeProfessores()
sistema.adicionar_professor("João", "Matemática")
sistema.adicionar_professor("Maria", "História")
sistema.listar_professores()
