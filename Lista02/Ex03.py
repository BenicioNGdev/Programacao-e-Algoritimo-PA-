peso = float(input("Digite o peso dos peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa}")
