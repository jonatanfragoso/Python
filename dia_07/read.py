# %%

nome_arquivo = "teste.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
open_file = open(nome_arquivo)

print(conteudo)
# %%

arquivo_2 = "teste2.txt"
txt = "Novo arquivo!"
with open(arquivo_2, mode="w") as open_file2:
    open_file2.write(txt)


# %%
