import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import numpy as np
import math

enemy = 1

def read_data(experiment_name):
    gain = []
    with open(experiment_name+'/gain.csv') as input:

        reader = csv.reader(input, delimiter=' ')
        next(reader)

        p_energy = []
        e_energy = []
        for rows in reader:
            p_health = float(rows[1])
            e_health = float(rows[2])
            gain.append(p_health - e_health)
    return gain

gain_best = []
gain_random = []
gain_no = []
for i in range(10):
    gain_best = np.hstack((gain_best,read_data(f'En{enemy}_select_best_{i}')))
    gain_random = np.hstack((gain_random,read_data(f'En{enemy}_select_random_{i}')))
    gain_no = np.hstack((gain_no,read_data(f'En{enemy}_no_isl_{i}')))

ticks = [1,2,3]
labels = ["Best migration", "Random migration", "No migration"]

<<<<<<< HEAD
fig = plt.figure(figsize=(15,4))
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)
ax1 = fig.add_subplot(1,1,1)
ax1.boxplot([gain_best, gain_random, gain_no])
=======
print(np.max(gain_best_1))
print(np.max(gain_best_2))
print(np.max(gain_best_3))
print(np.max(gain_random_1))
print(np.max(gain_random_2))
print(np.max(gain_random_3))
print(np.max(gain_no_1))
print(np.max(gain_no_2))
print(np.max(gain_no_3))

fig = plt.figure(figsize=(9,4))
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.0)
ax1 = fig.add_subplot(1,3,1)
ax1.boxplot([gain_best_1, gain_random_1, gain_no_1])
>>>>>>> 6dbc0d2509c21f5512a8edd182b8a7b14a423d7b
ax1.set_xticks(ticks, labels)
ax1.set_xticklabels(labels)
ax1.set_ylabel("Gain")
ax1.set_title(f"The gain per migration model on enemy {enemy}")
plt.show()
# ax2 = fig.add_subplot(1,2,2)
