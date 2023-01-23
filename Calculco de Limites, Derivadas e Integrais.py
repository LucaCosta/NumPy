# Cálculo de limite, derivada e integral usando a linguagem de programação Python.

# Author: Lucas Costa Fernandes
# Linkedin: https://www.linkedin.com/in/lucascostafernandes/
# GitHub: https://github.com/LucaCosta

import numpy as np # Chamando a biblioteca NumPy

# Definindo função
def f(x):
    return (x**2 + np.cos(2*x-1))

## Calculando Limite

print("Calculadora de limites")

valorX = float(input("Digite o valor de x a ser analisado: "))

n = 10000

# Limite pela direita
value_right = f(valorX+1/n)
print("Valor pela direita: ", value_right)

# Limite pela esquerda
value_left = f(valorX-1/n)
print("Valor pela esquerda: ", value_left)

# Atribuindo valor a delta
delta = 0.001

if abs(value_right - value_left) < delta: # Deixando o valor absoluto
    limite = np.floor(max(value_right, value_left)) # Definindo o valor máximo no ponto x0
    print("O valor máximo da função em x0 é: ", limite)

## Calculando Derivada

print("\nCalculadora de derivada")

# Zerando a variável x
x = 0

# Definindo função
def f2(x):
    return (x+4)*np.sin(x**2+3)

# Criando variáveis apartir do valor que o user escolhe
h = float(input("Escolha o valor do espaçamento h: "))
p = float(input("Escolha o valor do ponto p: "))

# Criando variável para derivar a função
derivada = (f2(p + h) - f2(p)) / h 

# Exibindo o resultado
print ("O resultado da derivada em p é: ", derivada)

## Calculando Integral

print("\nCalculadora de integral")

# Zerando a variável x
x = 0

# Definindo função
def f3(x):
    return np.tan(x**2)

pInicial = float(input("Escolha o ponto inicial: "))
pFinal = float(input("Digite o ponto final: "))
divisoes = int(input("Escolha a quantidade de divisões do intervalo: "))

h = ((pFinal - pInicial) / divisoes)

# print(h) # Mostra o valor de h

soma = 0

for i in range(0, n, 1):
    x = pInicial + h * i
    soma = soma + f3(x) * h

#Exibindo o resultado
print("O resultado é: ", soma)