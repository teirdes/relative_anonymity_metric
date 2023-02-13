# -*- coding: utf-8 -*-
"""
Loosely based on https://www.freehaven.net/anonbib/cache/Diaz02.pdf

within the context of IEEE 802.11 TGbi
"""

from numpy import array, zeros, full, arange, log2
from matplotlib.pyplot import subplots

def Diaz_Entropy(n, m, P):
    # ssd
    Q = P*log2(P)
    return sum(Q)

def Probability_Function(N, M):
    if M < N:
    # Pigeon hole principle
        AnonymitySetExists = (1-M/N)/(N-M)
        Vec = full(N, AnonymitySetExists)
        return [N, M, Vec]
    else:
        ProbabilityAnonymitySetTwo = 1/(M**2)
        Vec = full(N, 1-ProbabilityAnonymitySetTwo)
        Vec[0] = (N-1)*ProbabilityAnonymitySetTwo
        return [N, M, Vec]

NumberOfConfigurableBitsVisible = arange(2,16)
NumberOfConfigurations = 2**NumberOfConfigurableBitsVisible
NumberOfDevices = array([10, 100, 500])
Results = zeros((NumberOfConfigurations.size, NumberOfDevices.size))

for i in range (0, NumberOfConfigurations.size):
    for j in range (0, NumberOfDevices.size):
        P = Probability_Function(NumberOfDevices[j], NumberOfConfigurations[i]) 
        H_y = - Diaz_Entropy(P[0], P[1], P[2]) 
        H_max = log2(P[0]) 
        d = H_y/H_max
        Results[i, j] = round(100*d, 5)

print(Results)

fig, (ax1, ax2) = subplots(2,1)
ax1.plot(NumberOfConfigurableBitsVisible, Results[:,0], 'bo--')
ax1.set(xlabel='Visible free bits')
ax2.plot(NumberOfConfigurableBitsVisible[3:], Results[3:,0], 'bo--')
ax2.set(xlabel='Visible free bits')
fig.supylabel('Entropy scaled upp 100x')

fig, (bx1, bx2) = subplots(2,1)
bx1.plot(NumberOfConfigurableBitsVisible, Results[:,1], 'bo--')
bx1.set(xlabel='Visible free bits')
bx2.plot(NumberOfConfigurableBitsVisible[5:], Results[5:,1], 'bo--')
bx2.set(xlabel='Visible free bits')
fig.supylabel('Entropy scaled upp 100x')

fig, (cx1, cx2) = subplots(2,1)
cx1.plot(NumberOfConfigurableBitsVisible, Results[:,2], 'bo--')
cx1.set(xlabel='Visible free bits')
cx2.plot(NumberOfConfigurableBitsVisible[7:], Results[7:,2], 'bo--')
cx2.set(xlabel='Visible free bits')
fig.supylabel('Entropy scaled upp 100x')