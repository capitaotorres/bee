# subprograma
def fibo():
    sequencia = [0, 1]
    for m in range(61):
        ultimo = sequencia[-1]
        penultimo = sequencia[-2]
        soma = ultimo + penultimo
        sequencia.append(soma)
    o = int(input())
    print(f"Fib({o}) = {sequencia[o]}")
    print(sequencia)


# programa
fibo()
