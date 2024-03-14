def main():
    numeros = []  # Lista para armazenar os números digitados

    # Solicitação de entrada ao usuário
    while True:
        entrada = input("Digite um número (ou 'FIM' para encerrar): ")
        if entrada.upper() == "FIM":
            break  # Encerra o loop quando o usuário digita "FIM"
        try:
            numero = float(entrada)  # Converte a entrada para um número
            numeros.append(numero)  # Adiciona o número à lista
        except ValueError:
            print("Entrada inválida. Digite um número válido ou 'FIM'.")

    # Criando a nova lista com list comprehension
    nova_lista = [num * 3 for num in numeros]

    # Exibindo os resultados
    print("\nNúmeros digitados:", numeros)
    print("Nova lista (triplo dos valores):", nova_lista)

if __name__ == "__main__":
    main()
