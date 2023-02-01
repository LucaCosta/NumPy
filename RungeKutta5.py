import numpy as np
import pylab as plt

def f(P,t):
    r=0.8
    K=100
    valor = r*P*(1-P/K)
    return valor

a=0
b= 100
Num = 100 # Para diminuir o erro deve-se aumentar o valor de Num
h =(b-a)/Num
P = 0.5 # Xn

t_pontos  = np.arange(a,b,h)
P_pontos =[]
# Method of Runge kutta 5th

for i in t_pontos:
    P_pontos.append(P)
    k1 = h*f(P,i)
    k2 = h*f(P + h/4, i + k1/4)
    k3 = h*f(P + (3/8 * h), i + (3/32 * k1) + (9/32 * k2))
    k4 = h*f(P + (12/13 * h), i + (1932/2197 * k1) - (7200/2197 * k2) + (7296/2197 * k3))
    k5 = h*f(P + h, i + (439/216 * k1) - (8 * k2) + (3680/513) * k3 - (845/4104 * k4))
    P = P + (25/216 * k1) + (1408/2565 * k3) + (2197/4104 * k4) - k5/5
    

print(P_pontos[1])

plt.plot(t_pontos,P_pontos,color='#FF4500',linewidth=1.5, label='função dP/dt=P')
plt.ylim(0,110)
plt.title('Gráfico da função sigmóide')
plt.xlabel('t')
plt.ylabel('P(t)')
plt.grid(True)
plt.show()