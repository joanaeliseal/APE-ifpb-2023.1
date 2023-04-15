# Faça um programa que leia o nome de um aluno e as notas das três provas que ele
# obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).

nome = input("Informe o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3)/3

print(nome)
print(f"A média do estudante é: {media:.2f}")