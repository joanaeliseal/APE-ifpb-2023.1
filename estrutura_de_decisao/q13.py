# Escreva um programa que solicite a digitação de um ano e imprima sua classificação como
# bissexto ou não bissexto.
#Obs: um ano é bissexto se for divisível por 4, mas não por 100. Um ano também é bissexto se
# for divisível por 400.

ano = int(input('Informe o ano: '))

if ano % 4 == 0 or ano % 400 ==0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
