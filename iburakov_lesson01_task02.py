#---------------------------------------------------------------------------
#Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
#a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
#делится нацело на 7. Внимание: использовать только арифметические операции!
#b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
#списка, сумма цифр которых делится нацело на 7.
#c. * Решить задачу под пунктом b, не создавая новый список.

#----------------------------------------------------------------------------
odd_numbers = [] # список нечетных чисел
max_number = 1000 # максимальное число в списке нечетных чисел
sum_out1 = 0 # выходная сумма нечетных чисел
sum_out2 = 0 # выходная сумма нечетных чисел, увеличенных на 17

for i in range(max_number):
    if ((i + 1) % 2) != 0: # если число не четное
        cube1 = (i + 1) ** 3 # то вычисляем куб числа
        odd_numbers.append(cube1) # и формируем список кубов
        
        cube1 = str(cube1) # преобразуем в строковый вид для поиска суммы цифр
        local_sum = 0
        for j in range(len(cube1)):
            local_sum += int(cube1[j]) # ищем сумму цифр в кубе числа

        if (local_sum % 7) == 0: # если сумма цифр в кубе числа делится на цело на 7
            sum_out1 += int(cube1) # то ищем сумму кубов
        #----------------------------------------------
        cube2 = str(int(cube1) + 17) # увеличиваем куб числа на 17
        local_sum = 0
        for j in range(len(cube2)):
            local_sum += int(cube2[j]) # ищем сумму цифр в кубе числа

        if (local_sum % 7) == 0: # если сумма цифр в кубе числа делится на цело на 7
            sum_out2 += int(cube2) # то ищем сумму кубов

# Вывод данных ---------------------------------------------------------
print('sum1 = ', sum_out1, ', sum2 = ', sum_out2)
print('Список нечетных чисел : ', odd_numbers)
