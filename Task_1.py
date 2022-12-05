'''
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
Сложность задачи O(n), т.к. у нас один цикл.
Введенное число мы поделим на два если оно четное, в ином случае вычитаем единицу. В таком случае последним действием мы вычтем единицу из одного
'''

class Solution:
    def numberOfSteps(num):
        step = 0                            #Создаем переменную под количество действий
        while num != 0:                     #Создаем цикл который будет работать пока число не равно нулю
            if num % 2 == 0:                #Условие на четность
                step += 1
                num = num//2
            else:                           #Условие на нечетность
                step += 1
                num = num - 1
        return step                         #Выводим количество шагов

print(Solution.numberOfSteps(14))