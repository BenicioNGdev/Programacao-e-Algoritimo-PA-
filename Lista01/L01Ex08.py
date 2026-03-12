dias = int(input("Quantos dias você alugou o carro? "))
km = float(input("Quantos km você percorreu com o carro? "))
diasPreco = dias*60
kmPreco = km*0.15
PrecoTotal = kmPreco+diasPreco
print (f" Você deverá pagar R${PrecoTotal}")
