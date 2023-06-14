# Escreva uma função chamada primo para determinar se um número é primo ou não. A
# função deve receber um número inteiro, retornar True se o número for primo, ou False
# caso contrário.
# Escreva também um programa que, usando a função primo criada, exiba os números
# primos entre 1 e 100.

def primo(num):
    cont = 0
    for i in range(2,num+1):
        if num % i == 0:
            cont +=1
        if cont > 1:
            return False
        else:
            return True
        
# retornando os primos

for i in range(2,101):
    if primo(i) == True:
        print(i,'',end='')
