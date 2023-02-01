# This code is a solution for the differential equation dP/dt =P 

# Method of Runge Kutta 4th

import numpy as np
import pylab as plt

def f(P,t):
    valor = 10*np.exp(-((t-2)**2)/(2*(0.075)**2)) - 0.6 * P
    return valor

a=0
b= 4
Num = 100 # Para diminuir o erro deve-se aumentar o valor de Num
h =(b-a)/Num
P = 0.5

t_pontos  = np.arange(a,b,h)
P_pontos =[]
# Method of Runge kutta 4th

for i in t_pontos:
    P_pontos.append(P)
    k1 = h * f(P,i)
    k2 = h * f(P+0.5*k1, i+0.5*h)
    k3 = h * f(P+0.5*k2,i+0.5*h)
    k4 = h * f(P+k3,i+h)
    P += (k1+2*k2+2*k3+k4)/6

print(P_pontos[1])

plt.plot(t_pontos,P_pontos,color='#FF4500',linewidth=1.5, label='função dP/dt=P')
plt.title('Gráfico da função resolução do problema')
plt.xlabel('t')
plt.ylabel('P(t)')
plt.grid(True)
plt.show()