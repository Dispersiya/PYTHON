"""
1.Найти НОК двух чисел
2.Вычислить число Пи c заданной точностью d
Пример: при d = 0.001,  c= 3.141. 
3.Составить список простых множителей натурального числа N

4.Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
+ на тему файловой системы:
5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
"""
#1
"""
def calculate_lcm(x, y):
    if x > y: 
       greater = x 
    else: 
       greater = y 
    while(True): 
        if((greater % x == 0) and(greater % y == 0)): 
            lcm = greater 
            break 
        greater += 1 
    return lcm
num1 = int(input("Введите 1 число: ")) 
num2 = int(input("Введите 2 число: ")) 
print("НОК", num1,"и", num2,"=", calculate_lcm(num1, num2))
"""
#2
