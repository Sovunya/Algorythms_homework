'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Сложность задачи O(n^2)
Алгоритм проходится по списку сверяя его и если буквы сходятся то он добавляет значение в переменную
'''

class Solution:
    def numJewelsInStones(jewels,stones):
        number = 0                  #Количество повторений букв в списке
        for i in jewels:            #Цикл проходится по jewels
            for j in stones:        #Цикл проходится по stones
                if i == j:          #Если jewels равен stones добавляем один в numbers (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
                    number += 1
        return number
print(Solution.numJewelsInStones('aA','aAAbbbb'))