def calcular_imc(peso, altura):
    return peso / (altura ** 2)

pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input("Digite o nome da pessoa (ou digite 'fim' para encerrar): ")
    if pessoa['nome'].lower() == 'fim':
        break
    pessoa['altura'] = float(input("Digite a altura da pessoa em metros: "))
    pessoa['peso'] = float(input("Digite o peso da pessoa em quilogramas: "))
    pessoas.append(pessoa)

# Ordenar lista de pessoas por peso
pessoas_peso_ordenado = sorted(pessoas, key=lambda x: x['peso'])

# Contar pessoas com mais de 1.70m
pessoas_altura_superior_170 = sum(1 for pessoa in pessoas if pessoa['altura'] > 1.70)

# Calcular e adicionar IMC à lista de pessoas
for pessoa in pessoas:
    pessoa['imc'] = calcular_imc(pessoa['peso'], pessoa['altura'])

# Ordenar lista de pessoas por IMC
pessoas_imc_ordenado = sorted(pessoas, key=lambda x: x['imc'])

# Mostrar listagem ordenada por peso
print("\nListagem de pessoas ordenada por peso:")
for pessoa in pessoas_peso_ordenado:
    print(f"Nome: {pessoa['nome']}, Peso: {pessoa['peso']} kg")

# Mostrar quantidade de pessoas com mais de 1.70m
print("\nQuantidade de pessoas com mais de 1.70m:", pessoas_altura_superior_170)

# Mostrar listagem ordenada por IMC
print("\nListagem de pessoas ordenada por IMC:")
for pessoa in pessoas_imc_ordenado:
    print(f"Nome: {pessoa['nome']}, IMC: {pessoa['imc']:.2f}")
