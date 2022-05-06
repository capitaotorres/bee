a,b,c = map(int, input().split())
MaiorAB = (a+b+abs(a-b))/2
MaiorBC = (b+c+abs(b-c))/2
MaiorAB = int(MaiorAB)
MaiorBC = int(MaiorBC)
#MaiorCA = (c+a+abs(c-a))/2

if MaiorAB > MaiorBC:
    print(MaiorAB,"eh o maior")
else:
    print(MaiorBC,"eh o maior")