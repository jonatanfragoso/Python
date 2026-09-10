# %%

def f(x: int)->int:
    try:
        return 1 + x
    except:
        return "Erro. O valor precisa ser um inteiro."


x = f("dsdsd")
print(x)
# %%
def f(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("O valor precisa ser um inteiro.")
    return 1 + x


try:
    x = f(2)
    print(x)
except TypeError as e:
    print(e)

# %%

def teste(a, b, **kwargs):

    res = a *b
    for i in kwargs:
        print(i, kwargs[i])
        res = res * kwargs[i]
    return res
teste(2,2,test=0.5)
# %%
def kwargs(**kwargs):
    
    return kwargs
# kwargs(testando=1, teste2=2)
x = kwargs(testando=1, teste2=2)
print(x)
print(x)
# %%
