import matplotlib.pyplot as plt

def plot_hc(city, best_solution, eachiteration, best_value):
    x = []
    y = []
    for each_city in range(int(city)):
        x.append(best_solution[each_city][1])
        y.append(best_solution[each_city][2])
    x.append(best_solution[0][1])
    y.append(best_solution[0][2])
    
    plt.cla()
    plt.title('Hill Climbing' + ' ' + str(eachiteration) + ' ' + str(best_value))
    plt.plot(x, y, 'r')
    plt.pause(0.05)

def plot_sa(city, best_solution, eachiteration, best_value):
    x = []
    y = []
    for each_city in range(int(city)):
        x.append(best_solution[each_city][1])
        y.append(best_solution[each_city][2])
    x.append(best_solution[0][1])
    y.append(best_solution[0][2])
    
    plt.cla()
    plt.title('Simulated Annealing' + ' ' + str(eachiteration) + ' ' + str(best_value))
    plt.plot(x, y, 'r')
    plt.pause(0.1)