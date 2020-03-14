# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins

# this function computes the minimum number of coins needed to change the given value (money)
# into coins with denominations 1, 3, and 4 (array coins)
# this function uses caching (dictionary min_num_coins) to avoid re-computation
def change(money, coins, min_num_coins):

    # if money = 0, there is no change required
    min_num_coins[0] = 0
    # if the min number of coins required for the passed in money value
    # has been computed previously and, therefore, already exists in the dictionary min_num_coins,
    # return that value and bypass re-computation
    if money in min_num_coins.keys():
        return min_num_coins[money]

    # otherwise, make a recursive call to change()
    # and update the min_num_coins accordingly
    else:
        for m in range(1, money+1):
            min_num_coins[m] = float('inf') # set min_num_coins to infinitive
            # iterate through all coin denominations to find the min_num_coins
            for i in range(len(coins)):
                if m >= coins[i]:
                    num_coins = change(m - coins[i], coins, min_num_coins) + 1
                    if num_coins < min_num_coins[m]:
                        min_num_coins[m] = num_coins

    return min_num_coins[money]

if __name__ == '__main__':
    amount = int(input())
    min_num_coins = {}
    coins = [1, 3, 4]
    print(change(amount, coins, min_num_coins))
