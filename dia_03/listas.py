# %%

idades = [24, 56, 76, 23, 44, 22, 34, 49]
print(idades)
print(idades[2])
print(sum(idades)/len(idades))

#fatiar elementos
print(idades[0:3])
print(idades[-2:])

print(idades[::-1]) #terceira posição é o salto
print(idades[::2])
print(idades[::-2])

# %%
#NAVEGAR EM UMA LISTA
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]
numero = int(input("Entre com um número: "))

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print(f"Quantidade de {numero}: {contador}")
# %%
