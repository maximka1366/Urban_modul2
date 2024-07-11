control_input = True
while control_input:
    num = int(input('Введите число в первом поле: '))
    if num in range(3, 21):
        control_input = False
        kod = []
        lim_cycle_for = (num + 1) // 2
        for i in range(1, lim_cycle_for):
            j = i + 1
            while i + j <= num:
                if num % (i + j) == 0:
                    kod.append(i)
                    kod.append(j)
                j += 1
    else:
        print('Введено число должно бытбь от 3 до 20 !!!!!')
        print('Повторите ввод')
print('Для числа  в первом поле:', num, '    Пароль: ', * kod)