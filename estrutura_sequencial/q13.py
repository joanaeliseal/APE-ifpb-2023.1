# Escreva um programa que, dado um número inteiro representando uma quantidade de
# segundos, calcule quantas horas, minutos e segundos estão contidos nesta quantidade.
# Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.
# 1h = 3.600s
# 1h = 60min
# 1min = 60s

numero = int(input("Digite um número inteiro: "))

horas = numero // 3600
resto_minutos = numero % 3600 #resto
minutos = resto_minutos // 60
segundos = minutos % 60