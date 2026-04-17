la = float(input("Digite o primeiro lado: "))
lb = float(input("Digite o segundo lado: "))
lc = float(input("Digite o terceiro lado: "))

if la + lb > lc and la + lc > lb and lb + lc > la:
    if la == lb and lb == lc:
        print("Triângulo equilátero")
    elif la == lb or la == lc or lb == lc:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não forma um triângulo")