from math import *
print(pow(2,5))


import datetime

agora = datetime.datetime.now()
print("data e hora atuais:", agora)

data = datetime.datetime(2023, 12, 25)
print("data especifica:", data)

import random

print("numero inteiro aleatorio:", random.randint(1,100))

import os

print("nome do sistema operacional:", os.name)

print("caminho atual:", os.getcwd())

print("arquivos e direitorios:", os.listdir)


import requests

resposta = requests.get("https://api.github.com")
print("status code:", resposta.status_code)

print("conteudo da resposta:", resposta.text)

import pandas as pd

data = {'nome':['alice', 'bob', 'charlie'], 'idade':[25, 30,35]}
df = pd.DataFrame(data)
print("dataFrame:/n", df)

df_csv = pd.read_csv('caminho_para_arquivocsv')
print("DataFrame do CSV:/n", df_csv)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.title('grafico de linha')
plt.show()
