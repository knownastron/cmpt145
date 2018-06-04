# CMPT 145: Linear ADTs
# Application: M/M/1 Queuing simulation
# (based on example by Sedgewick, Wayne, Dondero)
#
# Simulate the arrival and service of customers using a queue.
# Calculate the average wait time for customers, given 
# assumptions about the rate of arrival and service.

import TQueue as Queue
import Statistics as Statistics
import random as rand

# the assumptions
arrival_rate = 1 # the number of customer arrivals per minute
service_rate = 2  # the number of customers served per minute
sim_length = 10000  # the end of the simulation in minutes


def sample_time(x):
    '''
    Return a random sample time until an event.
    In the long run, the events will have a rate of x
    events per unit time.

    Preconditions:
        x: the desired arrival rate, per unit time
    Post-conditions:
        none
    Return:
        a random sample time that obeys the rate x
    '''
    return rand.expovariate(x)


# customers wait in a service queue
service_queue = Queue.create()

# we're interested in the average time in the queue
waiting = Statistics.create()

# keep track of when the next customer will appear
nextArrival = sample_time(arrival_rate)

# keep track of when the next customer's service is done
nextService = nextArrival + sample_time(service_rate)


# simulate the arrival-service process
while nextService < sim_length:

    # new customers may arrive while a customer is being served
    while nextArrival < nextService:
        Queue.enqueue(service_queue, nextArrival)
        nextArrival = nextArrival + sample_time(arrival_rate)

    # serve the first customer in the queue
    this_arrival = Queue.dequeue(service_queue)

    # how long was the customer waiting?
    waited = nextService - this_arrival
    Statistics.add(waiting, waited)

    # determine when service to the next customer will end
    if Queue.is_empty(service_queue):
        nextService = nextArrival + sample_time(service_rate)
    else:
        nextService = nextService + sample_time(service_rate)

print('Average wait time:', Statistics.mean(waiting))
