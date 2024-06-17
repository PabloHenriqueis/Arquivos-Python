'''


A = [randint(1,10) for _ in range (50)]
B = [randint(1,10) for _ in range (50)]

plt.scatter(A, B)
plt.xlabel('navios')
plt.ylabel('contra-torpedeiros')
plt.title('dispersão N e C')
plt.show()
'''



''' 
import matplotlib.pyplot as plt
from random import randint

A = [1, 3, 10, 4, 2, 17, 19]
B = [1, 2, 10, 9, 4, 21, 14]
C = [1, 4, 10, 6, 0, 11, 12]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(A, B, C )

ax.set_xlabel('tempo')
ax.set_ylabel('quantidade')
ax.set_zlabel('terceiro dimensao')
ax.set_title('grafico')

plt.show()

A = ['jacke', 'jamess']
B = [8.2, 9.3]

plt.bar(A, B)
plt.xlabel('nome')
plt.ylabel('media')
plt.title('media de notas')
plt.show()
#plot = grafico em linha
'''

import matplotlib.pyplot as plt
