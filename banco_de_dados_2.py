import pymysql
import matplotlib.pyplot as plt


conexao = pymysql.connect (
host = 'localhost',
user = 'root',
password = '',
database = 'aluno_P_' #nome da pasta
)

'''
cursor = conexao.cursor()

cursor.execute('SELECT * FROM funcionários WHERE ID <= 10')
dados = cursor.fetchall()

ids = [info[0] for info in dados]
nomes = [info[1] for info in dados]
salario = [info[2] for info in dados]
cursor.close()


plt.bar(nomes, salario, color='green')
plt.xlabel('nomes')
plt.ylabel('salarios')
plt.show()
'''

'''
salario_novo = float(input('insira nova quantia de salario:'))
nome = str(input('nome do funcionário: '))

cursor = conexao.cursor()

cursor.execute('UPDATE funcionários SET salario = %s WHERE nome = %s', (salario_novo, nome))
conexao.commit()

cursor.close()
for nome in nomes:
    print(nome)
print('seu salario foi alterado com sucesso')


'''
