# Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua média e seu conceito.
# O programa deve conter as seguintes funções:
# • Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua
# média (aritmética).
# • Uma função que receba como parâmetro a média do aluno e retorne o seu
# conceito, de acordo com a tabela

def media(n1,n2,n3):
  return (n1+n2+n3)/3

def conceito(media):
  if media>=8:
    return 'A'
  elif media >=5:
    return 'B'
  else:
    return 'C'

nota1 = float(input('Digite a 1a nota: '))
nota2 = float(input('Digite a 2a nota: '))
nota3 = float(input('Digite a 3a nota: '))

med = media(nota1,nota2,nota3)
print(f'MÉDIA = {med} e CONCEITO {conceito(media)}')