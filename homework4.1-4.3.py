'''
1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

Для тех, кто только сейчас видит этот файл, вместо 1 задачи:
Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность 
и содержащие максимальное количество элементов. 
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
 [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
 Порядок элементов менять нельзя
2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
3.Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0. 
(решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).
'''
'''
#1
#nums = [3, 1, 2, 3, 4, 6, 1, 7]
nums= [1, 5, 2, 3, 4, 6, 1, 7]


def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))
'''
#2
'''
import random

with open('4.2.txt','w') as f:
    for a in range(15):
        number = random.randint(0, 1001)
        f.write(str(number))
        f.write("\n")
with open('4.2.txt','r') as f2:
    arr = []
    a = 0
    n = f2.readline()
    s = int(n)
    for i in f2:
        arr.append(int(i))
    print(arr)
    arr = sorted(arr)
print(arr)         
'''
#3
    
with open('Kints.txt','r') as file:
    arr = []
    i = 0
    n = file.readline()
    s = int(n)
    for i in file:
        arr.append(int(i))

def findTriplets(arr, n):

    for i in range(0, n-2): 

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])

n = len(arr)
findTriplets(arr, n)
