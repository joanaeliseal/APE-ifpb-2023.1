qtde = int(input('Informe quantos números serão fornecidos: '))
somatorio = 0

for k in range(qtde):
  valor = int(input(f'Digite o {k+1}º valor'))
  somatorio = somatorio + valor        # somatorio += valor; *= ; -= ; /= ; %= ;
print(f'O somatório é {somatorio}')