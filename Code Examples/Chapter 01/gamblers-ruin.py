"""
CMPT 145 Computing with Python Lists
The Gambler's Ruin Problem.

A gambler, starting with a given stake (some amount of money), and a goal
(a greater amount of money), repeatedly bets on a game that has a given
win probability; the game pays 1 unit for a win, and costs 1 unit for a loss.
The gambler will either reach the goal, or run out of money; it's just a
matter of time.

What is the probability that the gambler will reach the goal?
How many bets does it take, on average, to reach the goal or fall to ruin?
"""

import random as random
import time as time

stake = 10     # starting quantity of currency units
goal = 100      # goal to reach in currency units
n_trials = 10000    # number of trials to run
win_prob = 0.5  # probability of winning an individual game


def gamble(cash, goal, win_prob):
    """
    A single trial of a gambler playing games until they reach their
    goal (success) or run out of money (failure).

    cash: the gambler's initial amount of currency units.
    goal: the number of currency units to reach to be considered a win.
    win_prob: the likelihood of winning a single game.

    return: a tuple (outcome, bets):
        - outcome: the outcome of the trial (1 for success, 0 for failure)
        - bets: number of bets placed
    """

    # play games until goal is reached or no more currency units remain
    bets = 0  # number of bets placed so far
    while cash > 0 and cash < goal:
        bets += 1
        if random.random() < win_prob:
            cash += 1
        else:
            cash -= 1

    # return tuple of trial outcome, number of bets placed
    if cash == goal:
        return 1, bets
    else:
        return 0, bets


# run a number of trials while tracking trial wins & bet counts
bets = 0  # total bets made across all games from all trials
wins = 0  # total trials won
start = time.time()  # time at which we started the simulation
for t in range(n_trials):
    w,b = gamble(stake, goal, win_prob)
    wins += w
    bets += b
end = time.time()  # time at which we stopped the simulation

dur = end - start
# display statistics about the trials
print("Stake:", stake)
print('Goal:', goal)
print(str(100 * wins / n_trials) + '% wins')
print('Average # of bets made:',  str(bets / n_trials))
print('Number of trials:', n_trials)
print('Simulation took:', dur, 'seconds (about', n_trials/dur, 'trials per seconds)')
