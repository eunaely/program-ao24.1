# Inicializando a variável para armazenar a soma
soma = 0

# Loop de 1 a 500 (inclusive)
for numero in range(1, 501):
    # Verificando se o número é múltiplo de três
    if numero % 3 == 0:
        # Adicionando o número atual à soma
        soma += numero

# Exibindo o resultado
print(f"A soma dos números múltiplos de três entre 1 e 500 é: {soma}")
