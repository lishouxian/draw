import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0,2.8,5.6,8.4,11.2,14])
y1 = np.array([1.483,1.476,1.472,1.476,1.465,0])
y11 = np.array([1.503,1.502,1.497,1.523,1.605,0])
x2 = np.array([0,1.01,2.16,2.91,2.94,3.95,4.99,6.05,7.03,8.09,9.30,10.71,12.21,14.00])
y2 = np.array([1.536,1.537,1.541,1.546,1.547,1.555,1.558,1.555,1.543,1.566,1.652,1.648,1.416,0])


from scipy.interpolate import make_interp_spline
x1new = np.linspace(x1.min(),x1.max(),300)
y1_new = make_interp_spline(x1,y1)(x1new)
y11_new = make_interp_spline(x1,y11)(x1new)
x2new = np.linspace(x2.min(),x2.max(),300)
y2_new = make_interp_spline(x2,y2)(x2new)


plt.plot(x1new,y1_new, 'r', label='Experiment_re')
plt.plot(x1new,y11_new,'g', label='Simulation_re')
plt.plot(x2new,y2_new,'b', label='Simulation')


plt.title("Comparison of Simulation, Simulation_re and Experiment_re")
plt.xlabel("X/mm")
plt.ylabel("Velocity(m/s)")
plt.legend()
plt.savefig("Com_e.png")
plt.show()
