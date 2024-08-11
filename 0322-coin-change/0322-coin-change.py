class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        targets = [0] * (amount + 1) # 0 to target amount

        for target in range(1, amount + 1):
            temp = []
            for coin in coins:
                left_amount = target - coin
                if left_amount >= 0 and targets[left_amount] != -1:
                    temp.append(1 + targets[left_amount])

            targets[target] = min(temp) if temp else -1

        return targets[-1]