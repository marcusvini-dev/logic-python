# Projeto: Sistema de Aluguel de Carros # Autor: Marcus Vinícius

dias = int(input('Quantidade de dias? ')) # O programa começa pedindo a quantidade de dias.

if dias <= 0: 
    print('Dados inválidos!') # Se a quantidade de dias for menor ou igual a zero o programa mostra "Dados inválidos!".
    exit() # O simbolo - exit() - especifica que após o valor de dias ser menor ou igual a zero o programa finaliza.

quilometragem = float(input('Quantos KM foram rodados? '))  # O programa pede a quantidade de quilometros 

if quilometragem <= 0: # Se a quilometragem for menor ou igual a zero o programa mostra "Quilometragem inválida!".
    print('Quilometragem inválida!')
    exit()  # O simbolo - exit() - especifica que após o valor de quilometros ser menor ou igual a zero o programa finaliza.


media_km = quilometragem / dias # A tarifa depende da média de KM rodados por dia.

if media_km <= 100:
    tarifa_km = 0.50
else:
    tarifa_km = 0.75

diaria = 100.00 # O valor da diária

valor_diarias = diaria * dias
valor_quilometragem = quilometragem * tarifa_km

total = valor_diarias + valor_quilometragem

# Os valores de maneira detalhada
print('\n===== RESUMO DO ALUGUEL =====')
print(f'Quantidade de dias: {dias:.0f}') # O simbolo de :.0f , simboliza que após exibe o "." ou "," possua zero casas decimais.
print(f'Quilometragem rodada: {quilometragem:.2f} KM') # O simbolo de :.2f , simboliza que após exibe o "." ou "," possua duas casas decimais.
print(f'Tarifa por KM: R$ {tarifa_km:.2f}')
print(f'Valor das diárias: R$ {valor_diarias:.2f}')
print(f'Valor da quilometragem: R$ {valor_quilometragem:.2f}')
print(f'Valor total: R$ {total:.2f}')
