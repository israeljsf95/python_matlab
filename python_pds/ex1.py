# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:16:34 2020

@author: israe
"""

import numpy as np
import wave
import pyaudio as pa
import matplotlib.pyplot as plt

#teste preditor linear detio juju no python 
sinal1 = wave.open('ai.wav', 'rb')
fs = sinal1.getframerate()
data = sinal1.getnframes()

p = pa.PyAudio()
stream = p.open(format=pa.paFloat32,
                channels=1,
                rate=fs,
                output=True)

#filtrando o sinal por um passa alta

data_alta = data[1:-1] - 0.95*data[0:-2] 

stream.write(0.5*data/np.max(np.abs(data)))
stream.stop_stream()
stream.close()

p.terminate()


jan = np.round(0.035*fs).astype(int)
avan = np.round(0.010*fs).astype(int)

ordem = round(0.001*fs)

cp = []
pot = []
tcz = []

for k in range(0, (len(data_alta) - jan) + 1, avan):
    saux = data_alta[k:k+jan]
    pot.append(np.mean(saux**2))
    pz = np.where((saux[1:-1] > 0) & (saux[0:-2] < 0))
    tcz.append(len(pz)*fs/jan)
    S = []
    for m in range(0, ordem):
        S.append(saux[m:len(saux)- ordem + m])
    S = np.array(S)       
    C = np.linalg.pinv(S.T[:,0:-2])
    CC = C.dot(S.T[:,0:-1])
    cp.append(CC)
    
#reconstruindo
    
k = len(data)

perfil_tempo = 0.1 + 4*np.arange(0,k+1)/k
apontador = np.floor(np.cumsum(perfil_tempo)).astype(float)

N = apontador[-1]    
perfil_F0 = 80 - 30*(np.arange(0,N+1))/N
r = np.random.normal(size = np.arange(1,N+1).shape)
v = np.zeros(shape = r.shape)

pp = np.round(fs/perfil_F0[0]).astype(int)
print(pp)
v[pp-1] = 1; 

while pp < N:
    print(pp)
    pp = pp + np.round(fs/perfil_F0[pp-1]).astype(int)
    v[pp-1] = 1
    
    

N1 = fs*0.001
N2 = fs*0.0005

g = []
g.append(0.5*(1-np.cos(np.pi*np.arange(0,N1+1)/N1)))      
print(g)
g.append(np.cos(np.pi*np.arange(0,N2+1)/(2*N2)))
print(g)

g = np.array(g)
print('g antes de stack: ', g.shape)
g = np.hstack((g[0],g[1]))  
print('g depois de stack: ', g.shape)
vv = np.convolve(g, v)
v = v/np.std(v)
y = np.zeros(shape = r.shape)

orddem, ncol  = np.array(cp).T.shape
passo = np.floor(k/ncol).astype(int)
n_ini = ordem + 1
print(n_ini)
for col in np.arange(0, ncol):
#    print(col)
    if tcz[col] < 2000:
        vozeado = 0.9
    else:
        vozeado = 0.1
    ganho = np.sqrt(pot[col])
    n_fim = apontador[passo*col]
#   print(n_fim)
    for n in np.arange(n_ini, n_fim+1).astype(int):
#        print(n)
        y[n] = y[n-1:n-orddem-1:-1].dot(cp[col][-1:-len(cp[0])-1:-1]) + ganho*(vozeado*v[n] +(1-vozeado)*r[n])
    n_ini = n_fim

y = y/np.max(np.abs(y))



# play. May repeat with different volume values (if done interactively) 

plt.plot(y)        
        
        
        
        
        

