def main():
    valores = []  # Lista para armazenar os valores únicos

    for _ in range(10):
        try:
            valor = float(input("Digite um valor numérico: "))
            if valor not in valores:
                valores.append(valor)
            else:
                print("Valor já existe na lista. Não será adicionado novamente.")

        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    valores.sort()  # Ordena os valores em ordem crescente
    print("\nValores únicos digitados (em ordem crescente):")
    for v in valores:
        print(v)

if __name__ == "__main__":
    main()
