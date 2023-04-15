# Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
# se que nota1 possui peso 6 e nota2 possui peso 4.
# Mp = [(N1+P1) + (N2*P2) + ... / (P1 + P2 + P3)]

PESO_NOTA1 = 6.0
PESO_NOTA2 = 4.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_ponderada = (nota1*PESO_NOTA1)+(nota2*PESO_NOTA2)/PESO_NOTA1+PESO_NOTA2

print(f"A média ponderada é igual a: {media_ponderada:.2f}")