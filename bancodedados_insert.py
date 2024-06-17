import pymysql
import matplotlib.pyplot as plt


conexao = pymysql.connect (
host = 'localhost',
user = 'root',
password = '',
database = 'aluno_P_' #nome da pasta

)
'''
nome = str(input('informe o jogo: '))
ano = int(input('informe o ano: '))
preco = float(input('imforme o preco: '))

cursor = conexao.cursor()

cursor.execute('INSERT INTO Atividade (Jogo, Anodelancamento, preco)'
               'VALUES (%s, %s, %s)', (nome, ano, preco))
conexao.commit()

cursor.close()

print('seu jogo foi cadastrado com sucesso')
'''
cursor = conexao.cursor()

cursor.execute('SELECT * FROM Atividade ORDER BY Preco')
dados = cursor.fetchall()

ids = [info[0] for info in dados]
jogo = [info[1] for info in dados]
ano = [info[2] for info in dados]
precos = [info[3] for info in dados]
tamanho = len(ids)

cursor.close()

for info in range (0, tamanho):
    print(f'o {jogo[info]} foi lançado em {ano[info]} é custa {precos[info]}')