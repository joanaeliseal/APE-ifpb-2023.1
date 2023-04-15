# Faça um programa que efetue a apresentação do valor da conversão em real (R$)
# de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
# dólar e também a quantidade de dólares disponíveis com o usuário.

dolar = float(input("Informe o valor em dólar: "))
cotacao = float(input("Informe o valor da cotação: "))

conversao = dolar*cotacao

print(f"O valor da conversão de US${dolar}, com a cotação em R${cotacao}, é de R${conversao}.")