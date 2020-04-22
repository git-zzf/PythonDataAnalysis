import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("纵轴(值)")
plt.savefig('test', dpi=600)
plt.show()