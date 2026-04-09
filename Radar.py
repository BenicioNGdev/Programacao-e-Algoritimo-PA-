velocidade = int(input("Digite a velocidade: "))

if velocidade > 110:
    excesso = velocidade - 110
    multa = excesso * 5
    print(f"Multado! Valor: R$ {multa}")
else:
    print("Dentro do limite")