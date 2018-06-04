# CMPT 145 - Algorithms
# The Make Change Problem
#
# Given a number D in the range 0-99
# Find the smallest collection of coins whose value is D



# a greedy solution, adding coins one at a time
def change_v1(cents):
    """
    Purpose:
        Make change for the given cents value.
        Assumes coin values 25c, 10c, 5c, 1c
    Pre-conditions:
        :param cents: an integer
    Return: 
        a list of counts for the coins used.
    """
    coins = [25, 10, 5, 1]
    coin_index = 0
    counts = [0, 0, 0, 0]
    remaining = cents
    while remaining > 0:
        if coins[coin_index] <= remaining:
            counts[coin_index] += 1
            remaining -= coins[coin_index]
        else:
            coin_index += 1
    return counts


# a greedy solution, calculating each quantity
# of coins exactly
def change_v2(cents):
    """
    Purpose:
        Make change for the given cents value.
        Assumes coin values 25c, 10c, 5c, 1c
    Pre-conditions:
        :param cents: an integer
    Return: 
        a list of counts for the coins used.
    """
    coins = [25, 10, 5, 1]
    coin_index = 0
    counts = [0] * len(coins)
    remaining = cents
    while remaining > 0:
        counts[coin_index] = remaining // coins[coin_index]
        remaining = remaining % coins[coin_index]
        coin_index += 1
    return counts


# A brute force solution
# Find the smallest of all combinations of coins
def change_v3(cents):
    """
    Make change for the given cents value.
    Assumes coin values 25c, 10c, 5c, 1c
    :param cents: an integer
    :return: a list of counts for the coins used.
    """

    coins = [25, 10, 5, 1]

    def combinations(counts):
        """
        Cycle through every possible combination, looking
        for a combo that adds up to the right value, and 
        has the smallest number of coins
        :param counts: a 4-tuple
        :return: a pair (True, list) if list is the best 
                 combination
        """
        value = sum([counts[i] * v for i, v in enumerate(coins)])
        if value == cents:
            return True, counts
        elif value > cents:
            # don't add more coins to this combination
            # because it's already too big
            return False, None
        else:
            (c0, c1, c2, c3) = counts
            # add 1 to each number of coins separately
            trying = [(c0 + 1, c1, c2, c3), (c0, c1, c2 + 1, c3),
                      (c0, c1 + 1, c2, c3), (c0, c1, c2, c3 + 1)]
            # try to find the best combination, by using
            # the lowest number of coins
            best_size = 100
            best_counts = None
            for combo in trying:
                flag, res = combinations(combo)
                if flag and sum(res) < best_size:
                    best_size = sum(res)
                    best_counts = res
            if best_size == 100:
                # nothing worked!
                return False, None
            else:
                return True, best_counts

    flag, result = combinations((0, 0, 0, 0))
    if flag:
        return result
    else:
        return None


if __name__ == '__main__':
    examples = [0, 25, 37, 49, 51, 87, 99, 104]

    for e in examples:
        #print('Version 1:', e, change_v1(e))
        print('Greedy:', e, change_v2(e))
        #print('Version 3:', e, change_v3(e))

        print()
