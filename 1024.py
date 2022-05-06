"""
Entrada
A entrada contém vários casos de teste.
A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*10^4),
indicando a quantidade de linhas que o problema deve tratar.
As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.
"""
from audioop import reverse

'''def frases(word):
    qtd = int(input("Digite a quantidade de frases que deseja criptografar: "))
    for p in range(qtd):
        frase = str(input("Digite a frase a ser criptografada: "))
        frase.sort(reverse=True)
    return


'''
nomeEmPortugues = input()
deslocamento = int(input())
nomeDeslocamento = ""
for letra in nomeEmPortugues:
    nomeDeslocamento += chr(deslocamento - (ord(letra) - ord("a")))
    print(nomeDeslocamento)
    nomeDeslocamento.sort(reversed=True)
    #nomeDeslocamento += chr(deslocamento - (ord(letra)))
    #print(nomeDeslocamento)
    #nomeDeslocamento += chr(deslocamento)
    #print(nomeDeslocamento)

print(nomeDeslocamento)

