ticket = int(input('Укажите количество билетов:\t'))
visitor = 1
prise = 0
while visitor <= ticket:
    try:
        age = int(input(f'Укажите возраст поситителя для билета № {visitor}:\t'))
        if 0 <= age < 18:
            prise += 0
            visitor += 1
        elif 18 <= age <= 25:
            prise += 990
            visitor += 1
        elif age > 25:
            prise += 1390
            visitor += 1
        else:
            print('Возраст не может быть отрицательным')
    except ValueError:
        print('Укажите допустимое значение возраста')
        continue
if ticket > 3:
    prise = round(prise - prise / 10, 2)
    print(f'Общая стоимость билетов в рублях: {prise} с учётом 10% скидки, при покупки более трех билетов')
else:
    print(f'Общая стоимость билетов в рублях: {prise}')
