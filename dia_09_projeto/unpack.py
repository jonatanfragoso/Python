# %%
A = 1
B = 5


A,B = B,A

print(A)
print(B)
# %%
a, b, *c= 2, 3,45,5,345,345,345,35,3,53,6,4567,56,75,73635,6346

print(a, b, c)
# %%
def soma(*valores):
    return sum(valores)

v = [1,2,3,4]

soma = soma(*v)
soma
# %%
