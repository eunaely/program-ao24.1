import requests
from bs4 import BeautifulSoup

link = 'https://diatinf.ifrn.edu.br/docentes/'
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text, "html.parser")

professores = []

#  cada professor esteja em uma div com classe específica, como "professor"
for professor in site.find_all("h2"):
    nome = professor.get_text(strip=True)
    
    # encontrar a matrícula e o email
    matricula_tag = professor.find_next_sibling("span", class_="matricula")
    email_tag = professor.find_next_sibling("a", class_="email")

    matricula = matricula_tag.get_text(strip=True) if matricula_tag else "Matrícula encontrada"
    email = email_tag.get_text(strip=True) if email_tag else "Email encontrado"

    dados_professor = {
        "nome": nome,
        "matricula": matricula,
        "email": email
    }

    professores.append(dados_professor)

for prof in professores:
    print(f"Nome: {prof['nome']}, Matrícula: {prof['matricula']}, Email: {prof['email']}")
