def vetor():
    impar = []
    par = []
    for i in range(15):
        n = int(input())
        resto = n % 2
        if resto == 0:
            par.append(n)
        else:
            impar.append(n)

        if len(par) >= 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
        if len(impar) >= 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()

    for j in range(len(impar)):
        print(f"impar[{j}] = {impar[j]}")

    for j in range(len(par)):
        print(f"par[{j}] = {par[j]}")


# Programa principal
vetor()
