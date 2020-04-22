import matplotlib.pyplot as plt

plt.plot([0.3, 0.5, 0.8], [22.623, 46.316, 117.76], 'r', label='Simulation')
plt.plot([0.3, 0.5, 0.8], [24.23, 48.77, 125.37], 'g', label='Experiment')
plt.title("Comparison of Simulation and Experiment")
plt.xlabel("velocity(m/s)")
plt.ylabel("pressure(pa)")
plt.legend()
plt.savefig("Com_s_e.png")
plt.show()