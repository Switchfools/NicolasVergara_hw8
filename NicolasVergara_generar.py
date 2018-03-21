import numpy as np
#Se crea una función que retorna números segun una distribución de probabilidad definida a trozos.
def sample_1(N):
    #N Números random entre 0 y 1
    Sample=np.random.choice([-10, -5, 3, 9],size =N, p=[0.1, 0.4, 0.2, 0.3])
    return Sample
#Se crea una función que retorna números segun una distribución de probabilidad definida a trozos.
def sample_2(N):
    #N Números random que siguen distribución exponencial con betha=0.5
    betha=0.5
    Sample=np.random.exponential(scale=1/betha, size=N)
    return Sample
#Se crea una función que retorna una lista de M promedios , para N sampleos de cierta distribución, la función de sampleo debe ser ingresada como string
def get_mean(sampling_fun,N,M):
    Promedios=np.zeros(M)
    if(sampling_fun=='sample_1'):
        for i in range(M):
            Promedios[i]=np.sum(sample_1(N))/N
        return Promedios
    elif(sampling_fun=='sample_2'):
        for i in range(M):
            Promedios[i]=np.sum(sample_2(N))/N
        return Promedios
    else:
        return ('No sé ingresó una función de sampleo valida')
Samples=[10,100,1000]
for Samples in Samples:
    M=10000
    samples_1=get_mean('sample_1',M,Samples)
    samples_2=get_mean('sample_2',M,Samples)
    np.savetxt('sample_1_'+str(Samples)+'.txt', samples_1, delimiter=',')
    np.savetxt('sample_2_'+str(Samples)+'.txt', samples_2, delimiter=',')
