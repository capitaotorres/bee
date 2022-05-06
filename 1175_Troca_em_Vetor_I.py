def vetor():
    listinha = []
    for i in range(20):
        x = int(input())
        listinha.append(x)
    listinha.reverse()
    for i in range(20):
        print(f"N[{i}] = {listinha[i]}")
    return None


vetor()