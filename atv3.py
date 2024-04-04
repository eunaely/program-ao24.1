def calcular_juros_compostos(montante_inicial, taxa_juros, meses):
    montante_final = montante_inicial * (1 + taxa_juros) ** meses
    return montante_final

def main():
    # Solicitar entrada do usuário
    montante_inicial = float(input("Digite o montante inicial: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (em decimal): "))
    meses = int(input("Digite a quantidade de meses: "))

    # Calcular o montante final usando a função calcular_juros_compostos
    montante_final = calcular_juros_compostos(montante_inicial, taxa_juros, meses)

    # Imprimir o resultado na tela
    print("O montante final após", meses, "meses é:", montante_final)

if __name__ == "__main__":
    main()
