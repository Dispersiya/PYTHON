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
#2 Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 
'''
import math
d = "0.001"
d = int(len(d) - 2)
pi = round(math.pi, d)
print(pi)
print('{:.20}'.format(math.pi))
'''
#3.Составить список простых множителей натурального числа N
'''
import os
os.system("cls")

n = int(input('Введите число: '))
def prime_number (n):
    i = 2
    array = []
    while n != 1: 
        if n % i == 0:
            array.append(i) 
            n = n / i
            i = 2
        else: 
            i += 1
    return (array)
array = prime_number(n)
print(f'Список простых множителей натурального числа {n} = {array}')
'''
#4 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
'''
from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))
'''
#5 Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
import random

def create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator):
    with open(file_name, 'w') as data:
        for i in range(amount_of_numbers):
            sep = separator if i != amount_of_numbers - 1 else ""
            data.write(str(random.randint(min_value, max_value)) + sep)

def number_list_from_file(file_name, separator):
    with open(file_name, 'r') as data:
        list_numbers = list(map(int, data.read().split(separator)))
    return list_numbers

def delete_odd_numbers_from_list(list_numbers):
    return  [number for number in list_numbers if number % 2 == 0]

        
def write_odd_numbers_from_list(file_name, list_numbers, separator):
    with open(file_name, 'w') as data:
        data.write(separator.join(map(str, list_numbers)))
            
file_name = 'file.txt'
file_name_odd_numbers = 'odd_file.txt'
amount_of_numbers = 10
min_value = -7
max_value = 7
separator = " "
create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator)
list_numbers = number_list_from_file(file_name, separator)
list_numbers = delete_odd_numbers_from_list(list_numbers)
write_odd_numbers_from_list(file_name_odd_numbers, list_numbers, separator)