import pickle

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            lista_geral = pickle.load(arquivo)
        return lista_geral
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except pickle.PickleError:
        print("Erro: Ocorreu um problema ao ler o arquivo.")
        return []

def exibir_informacoes(lista_geral):
    if not lista_geral:
        print("Nenhuma informação encontrada para exibir.")
        return
    
    print("\nInformações restauradas do arquivo:")
    for i, pessoa in enumerate(lista_geral, start=1):
        nome, email = pessoa
        print(f"Pessoa {i}:")
        print(f"  Nome: {nome}")
        print(f"  E-mail: {email}\n")

def main():
    nome_arquivo = 'informacoes_pessoas.pkl'
    lista_geral = ler_arquivo(nome_arquivo)
    exibir_informacoes(lista_geral)

if __name__ == "__main__":
    main()
