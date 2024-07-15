class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)

        if length < 2:
            return 0

        # for day 1
        profit_if_i_sell_today = 0 # i dont have anything to sell on day-1
        profit_if_i_buy_today = -prices[0] # The money cut from pocket for the first investment

        # from day 2
        for i in range(1,length):
            # To sell, you musthave  bought it so take that amount, add current amount and remove transaction fee
            # we will consider only if it yields max sell profit
            profit_if_i_sell_today = max(profit_if_i_sell_today, profit_if_i_buy_today + prices[i] - fee)

            # If you buy today, it means you are investing from the current profit
            profit_if_i_buy_today = max(profit_if_i_buy_today, profit_if_i_sell_today - prices[i])

        return profit_if_i_sell_today
