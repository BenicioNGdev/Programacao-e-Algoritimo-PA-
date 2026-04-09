a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

maior = a
menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"Maior: {maior}")
print(f"Menor: {menor}")