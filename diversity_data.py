import csv
import numpy as np
import sys
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})

def plotdiversityislands(enemy, method):
    """select enemy from 1-3, method = 'random' or 'best'"""

    # make dicts to save the data per gen for diversity, mean and std
    data_mean = {}
    data_std ={}

    for i in range(0, 10):

        with open(f'En{enemy}_select_{method}_{i}/diversity.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=' ')
            current_row = 1

            div = []
            div_all_gens = []
            std_all_gens = []
            for row in reader:
                if current_row > 1:
                    div.append(int(row[2]))

                if (current_row != 1) and ((current_row-1) % 5 == 0):
                    
                    div_all_gens.append(np.mean(div))
                    std_all_gens.append(np.std(div))
                    div = []
                current_row += 1

            data_mean[f'run{i}'] = div_all_gens
            data_std[f'run{i}'] = std_all_gens

    # now we get the actual lists to plot the data by taking the averages of the averages and std's

    y_data = []
    y_error = []
    x_data = np.linspace(1,20,19)

    for i in range(0, 19):
        y = np.mean([data_mean['run0'][i], data_mean['run1'][i], data_mean['run2'][i], data_mean['run3'][i], \
            data_mean['run4'][i], data_mean['run5'][i], data_mean['run6'][i], data_mean['run7'][i], data_mean['run8'][i], data_mean['run9'][i] ])
        y_data.append(y)
        y_err = np.sqrt(sum([data_std['run0'][i]**2, data_std['run1'][i]**2, data_std['run2'][i]**2, data_std['run3'][i]**2, \
            data_std['run4'][i]**2, data_std['run5'][i]**2, data_std['run6'][i]**2, data_std['run7'][i]**2, data_std['run8'][i]**2, data_std['run9'][i]**2 ])/19)
        y_error.append(y_err)

    return y_data, y_error, x_data


def plotdiversity_no_islands(enemy):
    """plots diversity data for no islands, just the base model"""
    # make dicts to save the data per gen for diversity, mean and std
    data_mean = {}
    data_std ={}

    for i in range(0, 10):

        with open(f'En{enemy}_no_isl_{i}/diversity.csv') as csv_file:
            reader = csv.reader(csv_file, delimiter=' ')
            current_row = 1

            div = []
            div_all_gens = []
            std_all_gens = []
            for row in reader:
                if current_row > 1:
                    div.append(int(row[1]))

                if (current_row != 1) and ((current_row-1) % 1 == 0):
                    
                    div_all_gens.append(np.mean(div))
                    std_all_gens.append(np.mean(div))
                    div = []
                current_row += 1

            data_mean[f'run{i}'] = div_all_gens
            data_std[f'run{i}'] = std_all_gens

    # now we get the actual lists to plot the data by taking the averages of the averages and std's
    y_data = []
    y_error = []
    x_data = np.linspace(1,20,19)

    for i in range(0, 19):
        y = np.mean([data_mean['run0'][i], data_mean['run1'][i], data_mean['run2'][i], data_mean['run3'][i], \
            data_mean['run4'][i], data_mean['run5'][i], data_mean['run6'][i], data_mean['run7'][i], data_mean['run8'][i], data_mean['run9'][i] ])
        y_data.append(y)
        y_err = np.std([data_std['run0'][i], data_std['run1'][i], data_std['run2'][i], data_std['run3'][i], data_std['run4'][i], \
            data_std['run5'][i], data_std['run6'][i], data_std['run7'][i], data_std['run8'][i], data_std['run9'][i] ])
        y_error.append(y_err)

    return y_data, y_error, x_data

# make the plots here

enemy1_random = plotdiversityislands(1, 'random')
enemy1_best = plotdiversityislands(1, 'best')
enemy1_noisl = plotdiversity_no_islands(1)

enemy2_random = plotdiversityislands(2, 'random')
enemy2_best = plotdiversityislands(2, 'best')
enemy2_noisl = plotdiversity_no_islands(2)

enemy3_random = plotdiversityislands(3, 'random')
enemy3_best = plotdiversityislands(3, 'best')
enemy3_noisl = plotdiversity_no_islands(3)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, sharex=True, figsize=(10,4))

ax0.errorbar(enemy1_best[2], enemy1_best[0], enemy1_best[1], capsize=5, fmt='-o')
ax0.errorbar(enemy1_random[2], enemy1_random[0], enemy1_random[1], capsize=5, fmt='-o')
ax0.errorbar(enemy1_noisl[2], enemy1_noisl[0], enemy1_noisl[1], capsize=5, fmt='-o')
ax0.set_title('Enemy 1')
ax0.set_ylabel('Diversity', fontsize=22)
ax0.set_ylim(0, 30)

ax1.errorbar(enemy2_best[2], enemy2_best[0], enemy2_best[1], capsize=5, fmt='-o')
ax1.errorbar(enemy2_random[2], enemy2_random[0], enemy2_random[1], capsize=5, fmt='-o')
ax1.errorbar(enemy2_noisl[2], enemy2_noisl[0], enemy2_noisl[1], capsize=5, fmt='-o')
ax1.set_title('Enemy 2')
ax1.set_xlabel('Generation', fontsize=22)
ax1.set_ylim(0, 30)

ax2.errorbar(enemy3_best[2], enemy3_best[0], enemy3_best[1], capsize=5, fmt='-o', label='Best migr.')
ax2.errorbar(enemy3_random[2], enemy3_random[0], enemy3_random[1], capsize=5, fmt='-o', label='Random migr.')
ax2.errorbar(enemy3_noisl[2], enemy3_noisl[0], enemy3_noisl[1], capsize=5, fmt='-o', label='No migr.')
ax2.legend(loc='lower right')
ax2.set_title('Enemy 3')
ax2.set_ylim(0, 30)

fig.subplots_adjust(hspace=0, wspace=0.16)



plt.show()