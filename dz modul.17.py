# Функция сортировки
def sort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


# Функция поиска
def search(sort_num_list, num,  left, right):
    while right > left + 1:
        middle = (left + right) // 2
        if sort_num_list[middle] < num:
            left = middle
        else:
            right = middle
    return right


m = True
while m:
    try:
        num_list = list(map(int, input('Введите числа через пробел: ').split()))
        m = False
    except ValueError:
        print('Вы ввели недопустимое значение, попробуйте снова ввести числа через пробел')
        continue

m = True
while m:
    try:
        num = int(input('Введите число: '))
        m = False
    except ValueError:
        print('Вы ввели недопустимое значение, попробуйте снова ввести число')
        continue

# Сортировка
sort_num_list = sort(num_list)
print(sort_num_list)


if sort_num_list[0] > num:
    print(f'Введенное Вами число {num} меньше минимального в списке.')
elif sort_num_list[-1] < num:
    print(f'Введенное Вами число {num} больше максимального в списке.')
elif sort_num_list[0] == num:
    ID = search(sort_num_list, num, -1, len(sort_num_list))
    print(f'Число {sort_num_list[ID]} с индексом {ID} первое в списке.')
else:
    ID = search(sort_num_list, num, -1, len(sort_num_list))
    print(f'Число {sort_num_list[ID - 1]} с индексом {ID - 1},'
          f' число {sort_num_list[ID]} с индексом {ID}.')
