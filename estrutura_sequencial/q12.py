# Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
# bem como o número de litros de combustível gastos.
# Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a

LITRO = 5.09
hodometro_inicial = float(input("Informe a marcação inicial do Hodômetro: "))
hodometro_final = float(input("Informe a marcação final do Hodômetro: "))
litros_gastos = float(input("Informe os litros gastos na viagem: "))
tanque = float(input("Informe a capacidade do tanque: "))

#  a) Quilometragem rodada.
km = hodometro_inicial + hodometro_final
print(km)
#  b) Quantos quilômetros por litro faz o veículo.
km_litro = km / litros_gastos
# c) Autonomia do veículo: com o tanque cheio, consegue fazer quantos km?
autonomia = km_litro*tanque
# d) Custo da viagem.
custo = km*LITRO

print(f"Quilometragem rodada: {km}")
print(f"Quantos quilômetros por litro faz o veículo: {km_litro}")
print(f"Autonomia do veículo: {autonomia}")
print(f"Custo da viagem: {custo}")