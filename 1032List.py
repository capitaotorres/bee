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
localizarPessoa = primos[0]
#pessoas.sort(reverse=True)
pDel = 0
while len(pessoas) != 1 and len(primos) <= 3501:  # enquanto o número de pessoas for menor que 1 e primos até 3500
    print(primos[0])
    pDel = pDel + primos[0]
    if len(pessoas) >= primos[0]:
        del pessoas[-1*primos[0]+1]
        del primos[0]

        print(pessoas)

'''SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO
SOMAR OS INDEX ATÉ CHEGAR NO NUMERO PRIMO'''


