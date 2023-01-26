per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму"))
deposit = []
deposit.append(round(per_cent.get('ТКБ')/100*money))
deposit.append(round(per_cent.get('СКБ')/100*money))
deposit.append(round(per_cent.get('ВТБ')/100*money))
deposit.append(round(per_cent.get('СБЕР')/100*money))
print(deposit)
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать -', deposit_max)