import pymysql
import matplotlib.pyplot as plt


conexao = pymysql.connect (
host = 'localhost',
user = 'root',
password = '',
database = 'aluno_P_' #nome da pasta

)

cursor = conexao.cursor()

cursor.execute('SELECT * FROM Atividade WHERE ID <= 10')
dados = cursor.fetchall()

ids = [info[0] for info in dados]
nomes = [info[1] for info in dados]
ano = [info[2] for info in dados]
precos = [info[3] for info in dados]
cursor.close()

'''
print(ids)
print()
print()
print(dados)
for id in ids:
    print(id)
'''
for nome in nomes:
    print(nome)

plt.bar(nomes,precos)
plt.xlabel('nomes')
plt.ylabel('preço')
plt.show()