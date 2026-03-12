cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("A quantos anos você fuma cigarro? "))
dias = cigarros*(anos*365)
perda = dias/24/6
print (f" Você ja perdeu {perda} dias de vida, apenas consumindo cigarro! ")
