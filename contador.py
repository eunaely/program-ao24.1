# Lê a frase do usuário
frase = input("Digite uma frase: ")

# Converte a frase para letras maiúsculas para facilitar a contagem
frase_maiuscula = frase.upper()

# Conta quantas vezes a letra 'A' aparece na frase
quantidade_a = frase_maiuscula.count('A')

# Encontra a posição da primeira ocorrência da letra 'A'
primeira_posicao = frase_maiuscula.find('A') + 1  # Adiciona 1 para exibir a posição correta

# Encontra a posição da última ocorrência da letra 'A'
ultima_posicao = frase_maiuscula.rfind('A') + 1  # Adiciona 1 para exibir a posição correta

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
print(f"Ela aparece pela primeira vez na posição {primeira_posicao}.")
print(f"Ela aparece pela última vez na posição {ultima_posicao}.")
