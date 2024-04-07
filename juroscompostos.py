# Função para calcular juros compostos
def calcular_juros_compostos(montante_inicial, juros_mensais, quantidade_meses):
    montante_final = montante_inicial * ((1 + juros_mensais) ** quantidade_meses)
    return montante_final

# Função para gerar a lista de dicionários com o valor acumulado por mês
def gerar_lista_juros_compostos(montante_inicial, juros_mensais, quantidade_meses):
    lista_juros = []
    for mes in range(1, quantidade_meses + 1):
        valor_acumulado = calcular_juros_compostos(montante_inicial, juros_mensais, mes)
        lista_juros.append({"mes": mes, "valor": valor_acumulado})
    return lista_juros

# Solicita os dados do usuário e executa as funções
def main():
    montante_inicial = float(input("Digite o montante inicial do investimento: "))
    juros_mensais = float(input("Digite a taxa de juros mensais (em decimal): "))
    quantidade_meses = int(input("Digite a quantidade de meses do investimento: "))

    montante_final = calcular_juros_compostos(montante_inicial, juros_mensais, quantidade_meses)
    print(f"O montante final após {quantidade_meses} meses é: {montante_final:.2f}")

    lista_juros = gerar_lista_juros_compostos(montante_inicial, juros_mensais, quantidade_meses)
    print("\nListagem do mês com o valor acumulado:")
    for item in lista_juros:
        print(f"Mês {item['mes']}: {item['valor']:.2f}")

if __name__ == "__main__":
    main()
