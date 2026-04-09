valor_hora = float(input("Quanto você ganha por hora: "))
horas = float(input("Horas trabalhadas no mês: "))

bruto = valor_hora * horas

ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

descontos = ir + inss + sindicato
liquido = bruto - descontos

print(f"Salário Bruto: R$ {bruto}")
print(f"IR: R$ {ir}")
print(f"INSS: R$ {inss}")
print(f"Sindicato: R$ {sindicato}")
print(f"Salário Líquido: R$ {liquido}")
