import matplotlib.pyplot as plt
from random import randint


A = ['futbol', 'volei', 'luta' , 'natação' , 'basquete' ]
B = [15, 40, 15, 10, 20]

plt.pie(B, labels=A, autopct='%1.1f%%')
plt.title('historico de esportes')
plt.show()



'''

A = [randint(1,100) for _ in range (100)]
B = [randint(1,100) for _ in range (100)]

plt.scatter(A,B )
plt.xlabel('V a')
plt.ylabel('B')
plt.title('dispersão a e b')
plt.show()
'''


'''



plt.plot(A,B , color='silver', linestyle='--' ,marker='o' )
plt.xlabel('tempo')
plt.ylabel('velocidade')
plt.title('rendimento de motor')
plt.show()
#plot = grafico em linha
'''
'''import matplotlib.pyplot as plt

A = ['jacke', 'jamess']
B = [8.2, 9.3]

plt.bar(A, B)
plt.xlabel('nome')
plt.ylabel('media')
plt.title('media de notas')
plt.show()
#plot = grafico em linha
'''