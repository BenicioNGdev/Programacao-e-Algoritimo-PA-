preco = float(input("Informe o preço da mercadoria :"))
porcentagem = float(input("Digite a porcentagem de desconto :"))
PrecoFinal = preco*(porcentagem/100)
desconto = preco-PrecoFinal
print (f" O valor da mercadoria com {porcentagem}% de desconto, ficou custando R${desconto}, e seu desconto em R$ foi de {PrecoFinal}. ")
