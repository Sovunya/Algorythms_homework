'''
You are given an integer n, the number of teams in a tournament that has strange rules:
If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.
Во второй задаче аналогично сложность O(n). И как и в первой проводим примерно аналогичные действия
'''

class Solution:
    def numberOfMatches(n):
        match = 0                                                               #Создаем переменную под количество матчей
        all_matches = 0
        while n != 1:
            if n == 1:
                n = n/2                                                         #Количество комманд оставшихся после матча
                match = n                                                    #Счетчик
            else:
                if n % 2 == 0:                                                  #Если четное количество команд
                    n = n/2
                    match = n
                else:                                                           #Если нечетное количество команд
                    odd_teams = n - 1
                    n = odd_teams/2
                    match = n
                    n = n+1                                                     #Возвращаем нечетную команду
            all_matches += match                                                #Сохраняем количество команд
        return  int(all_matches)
print(Solution.numberOfMatches(14))