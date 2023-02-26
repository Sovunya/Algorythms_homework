class Solution:
    def getMaximumGenerated(self, n):
        if n < 2:                   #Проверяем чтобы n не было меньше двух
            return n

        nums = [0] * (n + 1)        #Создаем список nums который будет содержать сгенерированные числа
        nums[1] = 1
        maximum = 1

        for i in range(2, n + 1):   #Используем цикл for чтобы заполнить список nums в соответствии с заданными правилами
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            maximum = max(maximum, nums[i])

        return maximum
