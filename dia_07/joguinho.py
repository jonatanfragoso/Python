#loteria
# %%
import random

# %%
numero_sorteado = random.randint(1,15)
print(numero_sorteado)
tentativas = 3
while tentativas >= 1:
    chute = int(input("Entre com o seu palpite:"))
    if chute == numero_sorteado:
        print("Parabéns, você acertou o número!")
        break
    elif chute < numero_sorteado:
        if tentativas != 1:
            print(f"O seu chute é MENOR que o valor sorteado. Você tem mais {tentativas-1} tentativas.")
        else:
            print(f"O seu chute é MENOR que o valor sorteado. Você não tem mais tentativas. :(")
    else:
        if tentativas != 1:
            print(f"O seu chute é MAIOR que o valor sorteado. Você tem mais {tentativas-1} tentativas.")
        else:
            print(f"O seu chute é MAIOR que o valor sorteado. Você não tem mais tentativas. :(")
    tentativas -= 1

# %%