money = int(input("Введите сумму:"))
print(money)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

acc_TKB = money / 100 * per_cent['ТКБ']
acc_SKB = money / 100 * per_cent['СКБ']
acc_VTB = money / 100 * per_cent['ВТБ']
acc_SBER = money / 100 * per_cent['СБЕР']

deposit.append(int(acc_TKB))
deposit.append(int(acc_SKB))
deposit.append(int(acc_VTB))
deposit.append(int(acc_SBER))

bank_deposit['ТКБ'] = acc_TKB
bank_deposit['СКБ'] = acc_SKB
bank_deposit['ВТБ'] = acc_VTB
bank_deposit['СБЕР'] = acc_SBER

max_bank_deposit = max(bank_deposit, key=bank_deposit.get)

print(deposit)

print('Максимальная сумма, которую вы можете заработать —', str(max(deposit)),"|", 'В банке -', str(max_bank_deposit),)