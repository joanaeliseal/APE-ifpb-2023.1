# Cálculo do IMC
# IMC = peso/altura*altura

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso/(altura*altura)
print(f"{imc:.1f}")
print("Sua classificação é: ", end= "")

if imc >=40:
    print("Obesidade mórbida, CUIDADO")
elif (imc >= 35.0) and (imc <= 39.9):
    print("Sua classificação é: Obesidade Grau II")
elif (imc >= 30.0): # and (imc <= 34.9):
    print("Sua classificação é: Obesidade Grau I")
elif (imc >= 25.0): # and (imc <=29.9):
    print("Sua classificação é: Sobrepeso")
elif (imc >= 18.5): # and (imc <= 24.9):
    print("Sua classificação é: Peso normal")
else:
    print("Sua classificação é: Abaixo do peso")

