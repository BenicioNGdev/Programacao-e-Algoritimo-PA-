area = float(input("Digite a área a ser pintada (m²): "))

import math
litros = area / 3
latas = litros / 18
latas = math.ceil(latas) 
preco = latas * 80

print(f"Latas necessárias: {latas}")
print(f"Preço total: R$ {preco}")