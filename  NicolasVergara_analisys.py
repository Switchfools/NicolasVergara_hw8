import numpy as np
import matplotlib.pylab as plt
import glob
# se crea una función que retorne el valor de x para una distribución normal
Filenames=glob.glob('*.txt')
def normal_dist(x,mean,sigma):
    Constante_Normalización=1/(sigma*np.sqrt(2*np.pi))
    Normal=Constante_Normalización*np.exp(-(((x-mean)**2)/(2*(sigma**2))))
    return Normal
def get_fit(filename):
    DistribuciónExperimental=np.loadtxt(filename,delimiter=',')
    N=len(DistribuciónExperimental)
    Promedio=np.sum(DistribuciónExperimental)/N
    desviación=np.sqrt(np.sum(DistribuciónExperimental- Promedio)/(N-1))
    HistFreq=normal_dist(DistribuciónExperimental,Promedio,desviación)
    S=filename[:-3]+'.png'
    plt.figure()
    plt.hist(DistribuciónExperimental,facecolor='teal', alpha=0.75)
    plt.savefig(S)
    print(Promedio,desviación**2)

for i in range(len(Filenames)):
    get_fit(Filenames[i])
