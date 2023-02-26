class Solution:
    def countSmoothDescentPeriods(self, prices):
        descendant_count = 0
        previous_counts = 0
        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1] == 1:
                descendant_count += 1
                if previous_counts > 0:
                    descendant_count += previous_counts
                previous_counts += 1
            else:
                previous_counts = 0
        descendant_count += len(prices)
        return descendant_count
