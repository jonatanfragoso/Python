# %%
arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines()

for linha in data:
    print(linha)


# %%
dados = dict()
# print(dados)
chaves = data[0].strip("\n").split(";")

for i in chaves:
    dados[i] = []
    
# print(dados)

for c in data[1:]:
  
    valores = c.strip("\n").split(";")
   
    for j in range(0, len(valores)):
        dados[chaves[j]].append(valores[j])

print(dados)
# %%
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
media
# %%
