import random
import math
import matplotlib.pyplot as plt

class Lattice:
    def __init__(self, length, temperature):
        self.length = length
        self.temperature = temperature
        self.lattice_points = self.initialize_lattice()

    def initialize_lattice(self):
        lattice = []
        for x_loc in range(self.length):
            lattice.append([])
            for y_loc in range(self.length):
                spin = 1 if (random.random() >= 0.5) else -1
                lattice[x_loc].append(spin)
        return lattice

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

###Magnetism as it evolves with time
##N=100000
##m= []
##Lat = Lattice(16, 2.5)
##for i in range(N):
##    Lat.time_step()
##    m.append(Lat.magnetism())
##plt.plot(m)
##plt.show()

###Magnetism as a function of temperature
##Stabilize=10000
##T=2000
##N=500
##Lats=[]
##lattices=20
##temps = []
##for i in range(lattices):
##    temps.append(1+0.1*i)
##    Lats.append(Lattice(64, 1+.1*i))
##m=[]
##
##for i in range(lattices):
##    m1=0
##    for j in range(Stabilize):
##        Lats[i].time_step()
##    for j in range(N):
##        for k in range(T):
##            Lats[i].time_step()
##        m1=m1+abs(Lats[i].magnetism())
##    m1=m1/N
##    m.append(m1)
##plt.plot(temps,m)
##plt.title('<m> as a function of temperature (Lat size 32)')
##plt.ylabel('m')
##plt.xlabel('T')
##plt.show()

#Squared Magnetism as a function of temperature
def simulate(num_of_lattices = 20, lattice_size = 16, min_temperature=2, max_temperature=3, num_of_samples=5000, steps_between_samples=1000):
    Lattices = []
    temperatures = []
    m=[]
    m2=[]
    for i in range(num_of_lattices):
        temperatures.append(min_temperature + (max_temperature-min_temperature)/(num_of_lattices-1)*i)
        Lattices.append(Lattice(16, temperatures[i]))
        m.append([])
        m2.append([])



    
    for i in range(num_of_samples):
        for lattice in Lattices:
            for j in range(steps_between_samples):
                lattice.time_step()
        for j in range(num_of_lattices):
            m[j].append(Lattices[j].get_magnetization())
            m2[j].append(pow(Lattices[j].get_magnetization(), 2))

    avgM = []
    avgM2 = []
    suscept = []
    for i in range(num_of_lattices):
        avgM.append(0)
        avgM2.append(0)
        suscept.append(0)
        
        for j in range(num_of_samples):
            avgM[i] += abs(m[i][j])
            avgM2[i] += abs(m2[i][j])
        avgM[i] = avgM[i]/num_of_samples
        avgM2[i] = avgM2[i]/num_of_samples
        suscept[i] = num_of_samples*(avgM2[i] - pow(avgM[i], 2))/temperatures[i]
    plot_magnetism(temperatures, avgM, lattice_size)
    plot_susceptability(temperatures, suscept, lattice_size)

    
def plot_magnetism(temperatures, avgM, lattice_size):
    plt.plot(temperatures, avgM)
    plt.title("Magnetic Moments for Lattice Size : {}".format(lattice_size))
    plt.xlabel("Normalized Temperature (T/J)")
    plt.ylabel("Magnetization")
    plt.show()

def plot_susceptability(temperatures, susceptibilty, lattice_size):
    plt.plot(temperatures, susceptibility)
    plt.title("Susceptibility for Lattice Size : {}".format(lattice_size))
    plt.xlabel("Normalized Temperature (T/J)")
    plt.ylabel("Susceptability")
    plt.yscale('log')
    plt.show()
    
##Stabilize=100000
##time_steps=1000
##lattices=[]
##number_of_lattices=10
##temperatures = []
##average_over_time_steps = 100
##for i in range(len(lattices)):
##    temperatures.append(1+0.2*i)
##m=[]
##
##for i in range(len(lattices)):
##    Lats.append(Lattice(16, 1+.2*i))
##for i in range(len(lattices)):
##    msq=0
##    for j in range(Stabilize):
##        Lats[i].time_step()
##    for j in range(averaging):
##        for k in range(time_steps):
##            Lats[i].time_step()
##        msq=msq+pow((Lats[i].get_magnetic_moment()), 2)
##    msq=msq/averaging
##    m.append(m1)
##plt.plot(temperatures,m)
##plt.show()

###Susceptibility as a function of temperature
##Stabilize=10000
##T=2000
##Lat16=[]
##Lat32=[]
##Lat64=[]
###Lat128=[]
##
##lattices=20
##temps = []
##N=5000
##    
##m16=[]
##m32=[]
##m64=[]
###m128=[]
##
##for i in range(lattices):
##    temps.append(2+0.05*i)
##    Lat16.append(Lattice(16, 2+.05*i))
##    Lat32.append(Lattice(32, 2+.05*i))
##    Lat64.append(Lattice(64, 2+.05*i))
##    #Lat128.append(Lattice(128, 2+.05*i))
##
##for i in range(lattices):
##    m116=0
##    msq116=0
##    m132=0
##    msq132=0
##    m164=0
##    msq164=0
##    #m1128=0
##    #msq1128=0
##    for j in range(Stabilize):
##        Lat16[i].time_step()
##        Lat32[i].time_step()
##        Lat64[i].time_step()
##        #Lat128[i].time_step()
##    for j in range(N):
##        for k in range(T):
##            Lat16[i].time_step()
##            Lat32[i].time_step()
##            Lat64[i].time_step()
##            #Lat128[i].time_step()
##            
##        m116=m116+abs(Lat16[i].magnetism())
##        msq116=msq116+pow(Lat16[i].magnetism(),2)
##
##        m132=m132+abs(Lat32[i].magnetism())
##        msq132=msq132+pow(Lat32[i].magnetism(),2)
##
##        m164=m164+abs(Lat64[i].magnetism())
##        msq164=msq164+pow(Lat64[i].magnetism(),2)
##
##        #m1128=m1128+abs(Lat128[i].magnetism())
##        #msq1128=msq1128+pow(Lat128[i].magnetism(),2)
##
##    m116=m116/N
##    msq116=msq116/N
##    m16.append(N*(msq116-pow(m116,2))/Lat16[i].temperature)
##
##    m132=m132/N
##    msq132=msq132/N
##    m32.append(N*(msq132-pow(m132,2))/Lat32[i].temperature)
##
##    m164=m164/N
##    msq164=msq164/N
##    m64.append(N*(msq164-pow(m164,2))/Lat64[i].temperature)
##
##    #m1128=m1128/N
##    #msq1128=msq1128/N
##    #m128.append(N*(msq1128-pow(m1128,2))/Lat128[i].temperature)
##
##plt.plot(temps, m16, temps, m32, temps, m64)#, temps, m128)
##plt.yscale('log')
##plt.xlabel('Temperature')
##plt.ylabel('Susceptibility')
##plt.title('Susceptibility v. Temperature Lattices of 16, 32, and 64')#, and 128')
##plt.show()

##Susceptibility as a function of temperature one lattice
##Stabilize=10000
##T=2000
##Lat=[]
##
##lattices=20
##temps = []
##N=1000
##m=[]
##
##for i in range(lattices):
##    temps.append(2+0.05*i)
##    Lat.append(Lattice(32, 2+.05*i))
##
##for i in range(lattices):
##    m1=0
##    msq=0
##
##    for j in range(Stabilize):
##        Lat[i].time_step()
##    for j in range(N):
##        for k in range(T):
##            Lat[i].time_step()
##            
##        m1=m1+abs(Lat[i].magnetism())
##        msq=msq+pow(Lat[i].magnetism(),2)
##
##    m1=m1/N
##    msq=msq/N
##    m.append(N*(msq-pow(m1,2))/Lat[i].temperature)
##
##
##plt.plot(temps, m)
##plt.yscale('log')
##plt.show()


###Autocorrelation function
##Stabilize=10000
##iterations=5000
##MaxT=1000
##N=1000
##An=[]
##for t in range (MaxT):
##    An.append(0)
##for j in range (N):
##    Lat = Lattice(16, 2.8)
##    Aq=[]
##
##    for i in range (Stabilize):
##        Lat.time_step()
##    m=[]
##    for i in range (iterations):
##        Lat.time_step()
##        m.append(Lat.magnetism())
##
##    mavg=0    
##    msq=0
##    for i in range(iterations):
##        mavg+=m[i]
##        msq+=pow(m[i], 2)
##    mavg=mavg/iterations
##    msq=msq/iterations
##
##    for t in range(MaxT):
##        Aq.append(0)
##        for i in range(iterations-t):
##            Aq[t]+=m[t+i]*m[i]
##        Aq[t]=(Aq[t]/(iterations-t)-pow(mavg, 2))/(msq - pow(mavg, 2))
##    for t in range(MaxT):
##        An[t]+=Aq[t]
##        
##for t in range(MaxT):
##    An[t]=An[t]/N
##    
##plt.plot(An)
##plt.title("Autocorrelation as a Function of Temperature")
##plt.xlabel("Temperature")
##plt.ylabel('Correlation')
##plt.show()

