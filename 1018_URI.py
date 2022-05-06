"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser
decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas
necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo
fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a
mensagem: “Presentation Error”.
"""
N = int(input())
notas = 0
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0
n = N
if 0 < N < 1000000:
    for i in range(n):
        if n > 100:
            n = n - 100
            notas100 = notas100 + 1

        elif n >= 50:
            n = n - 50
            notas50 = notas50 + 1

        elif n >= 20:
            n = n - 20
            notas20 = notas20 + 1

        elif n >= 10:
            n = n - 10
            notas10 = notas10 + 1

        elif n >= 5:
            n = n - 5
            notas5 = notas5 + 1

        elif n >= 2:
            n = n - 2
            notas2 = notas2 + 1

        elif n >= 1:
            n = n - 1
            notas1 = notas1 + 1
print(N)
print(notas100, "nota(s) de R$ 100,00")
print(notas50, "nota(s) de R$ 50,00")
print(notas20, "nota(s) de R$ 20,00")
print(notas10, "nota(s) de R$ 10,00")
print(notas5, "nota(s) de R$ 5,00")
print(notas2, "nota(s) de R$ 2,00")
print(notas1, "nota(s) de R$ 1,00")
