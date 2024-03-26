# Recebendo as notas dos quatro bimestres
nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

# Calculando a média parcial
mparcial = nota1 + nota2 + nota3 + nota4

# Verificando o status do aluno
if mparcial >= 70:
    print("Status: Aprovado")
elif 20 <= mparcial < 70:
    print("Status: Recuperação")
    # Calculando a nota necessária para aprovação na recuperação
    nota_recuperacao = max(140 - mparcial, 0)
    print(f"Nota necessária na prova de recuperação: {nota_recuperacao:.2f}")
else:
    print("Status: Reprovado")
