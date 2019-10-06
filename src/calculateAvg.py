import numpy as np
import sys

which_algo = sys.argv[1]
run = sys.argv[2]
iteration = sys.argv[3]

data = []
for i in range(int(run)):
    temp = np.loadtxt('result/' + which_algo + '/' + which_algo + '-' + str(i+1) + '.txt', dtype=np.str, delimiter=",")
    data.append(temp)

for each_iteration in range(int(iteration)):
    total = 0
    for each_run in range(int(run)):
        total = total + float(data[each_run][each_iteration])
    total = total / int(run)
    print(str(each_iteration)+'	'+str(total))