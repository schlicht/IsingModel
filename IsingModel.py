import random
import math
import matplotlib.pyplot as plt

class Lattice:
    def __init__(self, length, temperature):
        self.length = length
        self.temperature = temperature
        self.lattice_points = self.initialize_lattice()

    # Creates lattice with spins either up or down
    def initialize_lattice(self):
        lattice = []
        for x_loc in range(self.length):
            lattice.append([])
            for y_loc in range(self.length):
                spin = 1 if (random.random() >= 0.5) else -1
                lattice[x_loc].append(spin)
        return lattice

    # Selects and changes one spin if energetically favorable or if meets a certain probability threashold
    def time_step(self):
        x_loc = int(random.random()*self.length)
        y_loc = int(random.random()*self.length)

        spin = self.lattice_points[x_loc][y_loc]

        above_spin = self.lattice_points[x_loc][((y_loc+1) % self.length)]
        right_spin = self.lattice_points[((x_loc+1) % self.length)][y_loc]
        below_spin = self.lattice_points[x_loc][((y_loc-1) % self.length)]
        left_spin  = self.lattice_points[((x_loc-1) % self.length)][y_loc]


        probability_of_flipping_spin =math.exp(-2*(spin*(left_spin+right_spin+above_spin+below_spin))/self.temperature)
        if(random.random()<probability_of_flipping_spin):
            self.lattice_points[x_loc][y_loc]= - spin

    def get_magnetization(self):
        return self.get_magnetic_moment()/math.pow(self.length, 2)


    def get_magnetic_moment(self):
        moment=0
        for x_loc in range(self.length):
            for y_loc in range(self.length):
                moment += self.lattice_points[x_loc][y_loc]

        return moment

def simulate(num_of_lattices = 20, lattice_size = 16, min_temperature= 1.5, max_temperature=3, num_of_samples=5000, steps_between_samples=1000):
    Lattices = []
    temperatures = []
    moments=[]
    moments_sq=[]
    
    for i in range(num_of_lattices):
        temperatures.append(min_temperature + (max_temperature-min_temperature)/(num_of_lattices-1)*i)
        Lattices.append(Lattice(16, temperatures[i]))
        moments.append([])
        moments_sq.append([])



    
    for i in range(num_of_samples):
        for lattice in Lattices:
            for j in range(steps_between_samples):
                lattice.time_step()
        for j in range(num_of_lattices):
            moments[j].append(Lattices[j].get_magnetization())
            moments_sq[j].append(pow(Lattices[j].get_magnetization(), 2))

    average_moment = []
    average_moment_sq = []
    susceptibility = []

    for i in range(num_of_lattices):
        average_moment.append(0)
        average_moment_sq.append(0)
        susceptibility.append(0)
        
        for j in range(num_of_samples):
            average_moment[i] += abs(moments[i][j])
            average_moment_sq[i] += abs(moments_sq[i][j])

        average_moment[i] = average_moment[i]/num_of_samples
        average_moment_sq[i] = average_moment_sq[i]/num_of_samples
        susceptibility[i] = num_of_samples/lattice_size*(average_moment_sq[i] - pow(average_moment[i], 2))/temperatures[i]
    
    #plot_magnetism(temperatures, average_moment, lattice_size)
    plot_susceptibility(temperatures, susceptibility, lattice_size)

    
def plot_magnetism(temperatures, average_moment, lattice_size):
    plt.plot(temperatures, average_moment)
    plt.title("magnetic moments for Lattice Size : {}".format(lattice_size))
    plt.xlabel("Normalized Temperature (T/J)")
    plt.ylabel("magnetization")
    plt.show()

def plot_susceptibility(temperatures, susceptibility, lattice_size):
    plt.plot(temperatures, susceptibility)
    plt.title("Susceptibility for Lattice Size : {}".format(lattice_size))
    plt.xlabel("Normalized Temperature (T/J)")
    plt.ylabel("susceptibility")
    plt.yscale('log')
    plt.show()

simulate()
