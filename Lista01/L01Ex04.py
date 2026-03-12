salario_antigo= float(input("Digite o valor do seu salário antigo: "))
porcentagem = float(input("Digite a porcentagem de aumento do seu salário: "))
salario_novo = salario_antigo*porcentagem/100+salario_antigo
QntAumento = salario_novo - salario_antigo
print (f" Seu Salário era de R${salario_antigo}, antes do aumento de {porcentagem}%, você teve um aumento de R${QntAumento} no seu salário e seu novo salário é de R${salario_novo}")
