# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# LISTA DE PRIMOS
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from audioop import reverse

numerosPrimos = 3501
primos = []
for i in range(2, numerosPrimos + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        primos.append(i)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# LISTA DE PESSOAS
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
numeroPessoas = int(input())
pessoas = []
for l in range(1, numeroPessoas + 1):
    pessoas.append(l)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# ELIMINANDO PESSOAS
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# pessoasEliminada = pessoas
p = primos[0]
pessoas.sort(reverse=True)
mult = 1
while len(pessoas) >= 1 and p <= 3501:  # enquanto o número de pessoas for menor que 1 e primos até 3500
    del pessoas[:p:]
    print(pessoas)
    print(p)
    '''
    pessoas.pop(len(pessoas) - p)
    print(pessoas)'''
    p = p + p

