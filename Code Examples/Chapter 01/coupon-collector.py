"""
CMPT 145 Computing with Python Lists
The Coupon Collector Problem

Suppose there are n coupons to collect, and coupons are obtained randomly
(with equal probability), with repeats allowed (replacement).

How many coupons need to be obtained before all coupons have been seen at least once?

(Not answered: how many on average?)
"""

import random as random
import time as time

start = time.time()
n = 100  # number of unique coupons to collect
n_trials = 2000

for i in range(n_trials):
    count = 0                   # number of total coupons collected
    collected_count = 0         # number of unique coupons collected
    is_collected = n*[False]    # list tracking status of unique coupons collected

    # keep collecting coupons until we collect at least one of every kind of coupon
    while collected_count < n:

        # obtain a random new coupon
        value = random.randrange(0,n)
        count += 1

        # if we obtained a new unique coupon, update status and count of unique coupons collected
        if not is_collected[value]:
            collected_count += 1
            is_collected[value] = True

end = time.time()
dur = end - start

# display number of total coupons collected
print("Total Coupons Collected:", count)
print("Coupons Collected per coupon:", count/n)
end = time.time()
dur = end - start
print('Number of coupons collected:', count/n)
print('Number of trials:', n_trials)
print('Time:', dur, dur/n_trials)
