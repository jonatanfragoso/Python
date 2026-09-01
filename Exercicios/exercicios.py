# %%
# Exercício 1. Produto Aritmético e Lógica Condicional
# Escreva uma função em Python que receba dois números inteiros.
# Se o produto dos dois números for menor ou igual a 1000, retorne o produto;
# caso contrário, retorne a soma.
print("Entre com dois números inteiros:")
n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
if((n1 * n2) <= 1000):
    print(f"O resultado é: {n1 * n2}")
else:
    print(f"O resultado é: {n1 + n2}")



# %%
#Exercício 2. Soma cumulativa de um intervalo
# Percorra os 10 primeiros números (0–9). Em cada iteração, 
# imprima o número atual, o número anterior e a soma deles.

numbers = 0

for i in range(10):
    if i == 0:
        print(f"Número atual: {i}")
    else:
        numbers = i + (i - 1)
        print(f"Número atual: {i}, Número anterior: {i - 1}, Soma: {numbers}")