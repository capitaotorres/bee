"""
beecrowd | 1064
Positivos e Média
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1 Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha,
deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números
será positivo.

Saída O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores
positivos digitados. """


def posi():
    media = 0
    p = 0
    for n in range(6):
        n1 = float(input())
        if n1 > 0:
            media = n1 + media
            p = p + 1
    media = media / p
    print(p, f"valores positivos\n{media:.1f}")
    return None


posi()
