import pickle

def obter_informacoes_pessoas():
    # Lista para armazenar as informações de todas as pessoas
    lista_geral = []

    print("Bem-vindo ao sistema de coleta de informações!")
    print("Por favor, insira o nome e o e-mail das pessoas.")
    print("Quando terminar, digite 'END' para encerrar a entrada.")

    while True:
        nome = input("Digite o nome da pessoa (ou 'END' para finalizar): ").strip()
        if nome.upper() == "END":
            break
        email = input("Digite o e-mail da pessoa: ").strip()
        
        # Cria uma lista com as informações da pessoa
        informacoes_pessoa = [nome, email]
        # Adiciona a lista de informações na lista geral
        lista_geral.append(informacoes_pessoa)
        
        print("Informações da pessoa adicionadas com sucesso!")

    return lista_geral

def salvar_em_arquivo(lista_geral, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(lista_geral, arquivo)
    print(f"As informações foram salvas com sucesso no arquivo '{nome_arquivo}'.")

def main():
    lista_geral = obter_informacoes_pessoas()
    nome_arquivo = 'informacoes_pessoas.pkl'
    salvar_em_arquivo(lista_geral, nome_arquivo)

if __name__ == "__main__":
    main()
