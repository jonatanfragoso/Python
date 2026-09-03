# %%

dados = {"nome":"Jonatan",
         "idade":34,
         "filhos":False,
         "formacao": ["Sistemas de Informação", "Teste com IA"],
         "cargos":[{"nome": "estagiario", "empresa":"UFAC"}]
         }

print(dados)
print(dados["nome"])
print(dados["formacao"])
print(dados["formacao"][-1])
print(dados["cargos"][0]["empresa"])

#FUNCAO PARA ATRIBUTOS
print("Chaves:", dados.keys())
print("Valores:", dados.values())
print("Items:", dados.items())
# %%
#PERCORRENDO UM DICIONÁRIO

for i in dados:
    print(i, "->", dados[i])
# %%
for chave, valor in dados.items():
    print(chave, "->", valor)
# %%
