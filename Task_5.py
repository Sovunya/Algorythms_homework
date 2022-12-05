'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
Сложность O(n) т.к. у нас всего один цикл

'''

class Solution:
    def removeOuterParentheses(s):
        answer = ""                                     #Создаем строку для ответа
        index = 0                                       #Создаем переменную для индексов
        stack = []                                      #Создаем список для хранения индексов

        while index < len(s):                           #Начинаем цикл
            if s[index] == '(':
                stack.append(index)
            elif s[index] == ')':
                index_remove = stack.pop()
                if not stack:                           #Если в списке становится пусто, то это были скобки второго уровня
                    answer += s[index_remove + 1:index] #Добавляем в ответ то, что было в скобках
            index += 1
        return answer

print(Solution.removeOuterParentheses("(()())(())"))

