peso = float(input("Digite o peso dos peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a pagar: R$ {multa:.2f}")
else:
    print("Peso dentro do limite permitido.")