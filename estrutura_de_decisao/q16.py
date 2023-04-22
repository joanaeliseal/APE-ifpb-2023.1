'''Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
foi aprovado ou não no concurso.'''

nome = input('Nome do candidato: ')
nota1 = float(input('Informe a nota da 1a etapa: '))
nota2 = float(input('Informe a nota da 2a etapa: '))

media1 = (nota1+nota2)/2

if media1 >= 7.0:
    print('Candidato apto para 2a etapa!')
    nota3 = float(input('Digite a nota da 2a etapa: '))
    if nota3 >= 8.0:
        print(f'Candidato APROVADO. Nota: {nota3:.1f}')
    else:
        print('Candidato REPROVADO.')
else:
    print('Candidato inapto para 2a etapa.')