# %%
frutas = {
    "Pera": "R$1,25",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,25",
    "Jaca": "R$5,25",
    "Laranja": "R$1,25",
    "Banana": "R$2,85",
    "Limão": "R$0,60",
    "Uva": "R$1,95",
}

fruta = input("Entre com o nome da fruta:")

if fruta in frutas:
    print(frutas[fruta])
else:
    print(f"Fruta não encontrada. Entre com um valor válido: {frutas.keys()}")




# %%
frases = {}

while True:
    frase = input("Entre com uma frase:")
    if frase == "":
        break
    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1

for i in frases:
    print(f"{i} -> {frases[i]}")


    
# %%
frases = {"oi": 2, "tchau": 1}

# renomear "oi" para "olá"
frases["olá"] = frases.pop("oi")

print(frases)  # {"tchau": 1, "olá": 2}
# %%
