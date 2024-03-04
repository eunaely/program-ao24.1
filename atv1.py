def main():
    # Entrada de dados
    largura = float(input("Digite a largura do cômodo (em metros): "))
    comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
    altura_parede = float(input("Digite a altura da parede (em metros): "))
    rendimento_tinta = float(input("Digite o rendimento da tinta (m²/litro): "))

    # Cálculo da área total das quatro paredes
    area_total = 2 * (largura + comprimento) * altura_parede

    # Quantidade de tinta necessária para duas demãos
    tinta_necessaria = area_total * 2 / rendimento_tinta

    print(f"\nSerão necessários aproximadamente {tinta_necessaria:.2f} litros de tinta para pintar as quatro paredes com duas demãos.")

if __name__ == "__main__":
    main()
