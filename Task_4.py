'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
Сложность задачи O(n*log(n)) из-за функции sort в коде который я напсал сам (´• ω •`)
Сначала находим минимальную разность, потом сравниваем разности с прошлым ответом и записываем пары этих чисел
'''

class Solution:
    def minimumAbsDifference(arr):
        max = 10 ^ 6                        #Максимальное значение по условию
        answer = []                          #Создаем переменную для ответа
        arr.sort()                          #Сортируем список
        for i in range(len(arr) - 1):       #Цикл для нахождения минимальной разности
            if arr[i+1] - arr[i] < max:
                max = arr[i + 1] - arr[i]

        for i in range(len(arr) - 1):       #Цикл для заполнения ответа парами минимальных разностей
            if arr[i+1] - arr[i] == max:
                answer.append((arr[i], arr[i + 1]))
        return answer

print(Solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))