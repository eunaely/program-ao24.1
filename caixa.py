def caixa_eletronico(valor_saque):

    if valor_saque <= 0 or valor_saque > 1000:
        return "Não é possível atender ao pedido."

    cedulas = [100, 50, 20, 10, 5]
    resultado = []

    for cedula in cedulas:
        qtd_cedulas = valor_saque // cedula
        valor_saque %= cedula
        resultado.append((cedula, qtd_cedulas))

    mensagem = ""
    for cedula, qtd in resultado:
        if qtd > 0:
            mensagem += f"{qtd} cédula(s) de R${cedula},00\n"

    return mensagem

# Exemplo de uso
valor_saque = int(input("Digite o valor que deseja sacar (limite de R$ 1.000,00): "))
print(caixa_eletronico(valor_saque))
