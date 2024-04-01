def calcular_imc(peso, altura):
    """
    Calcula o IMC com base no peso (em kg) e altura (em metros).
    """
    return peso / (altura ** 2)

def main():
    # Inicializa uma lista vazia para armazenar os dados das pessoas
    pessoas = []

    # Loop para ler os dados de várias pessoas
    while True:
        nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break

        altura = float(input("Digite a altura da pessoa (em metros): "))
        peso = float(input("Digite o peso da pessoa (em kg): "))

        # Cria um dicionário com as informações da pessoa
        pessoa = {
            "nome": nome,
            "altura": altura,
            "peso": peso,
        }

        # Adiciona o dicionário à lista de pessoas
        pessoas.append(pessoa)

    # Ordena a lista de pessoas por peso
    pessoas_ordenadas_por_peso = sorted(pessoas, key=lambda x: x["peso"])

    # Conta quantas pessoas têm mais de 1.70m
    pessoas_altas = sum(1 for pessoa in pessoas if pessoa["altura"] > 1.70)

    # Calcula o IMC para cada pessoa e ordena a lista por IMC
    for pessoa in pessoas:
        pessoa["imc"] = calcular_imc(pessoa["peso"], pessoa["altura"])

    pessoas_ordenadas_por_imc = sorted(pessoas, key=lambda x: x["imc"])

    # Exibe os resultados
    print("\nListagem ordenada por peso:")
    for pessoa in pessoas_ordenadas_por_peso:
        print(f"{pessoa['nome']}: {pessoa['peso']} kg")

    print(f"\nQuantidade de pessoas com mais de 1.70m: {pessoas_altas}")

    print("\nListagem ordenada por IMC:")
    for pessoa in pessoas_ordenadas_por_imc:
        print(f"{pessoa['nome']}: IMC {pessoa['imc']:.2f}")

if __name__ == "__main__":
    main()
