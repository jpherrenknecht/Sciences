import matplotlib.pyplot as plt
import numpy as np

#  graphique simple
# plt.plot([1, 2, 3, 4],[1,4,9,16],'ro')
# plt.ylabel('des nombres')

# graphiques avec 3 courbes tirets rouges - carres bleus - triangles verts
# t=np.arange(0.,5.,0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.show()


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()