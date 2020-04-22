import matplotlib.pyplot as plt

plt.plot([-10, -5, 0, 5, 10], [0, 0, 0, 5, 10])
plt.show()

plt.plot([-10, -5, 0, 0.00001, 5, 10], [0, 0, 0, 1, 1, 1])
plt.show()
print("ok")