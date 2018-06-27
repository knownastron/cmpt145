# CMPT 145: Linear ADTs
# Application: M/M/1 Queuing simulation
# (based on example by Sedgewick, Wayne, Dondero)
#
# Simulate the arrival and service of customers using a single queue.
# Calculate the average wait time for customers, given assumptions
# about the rate of arrival and service.

import Queue as Queue
import Statistics as Statistics
import random as rand
import ContainerS as Container


# the assumptions
arrival_rate =  1.9  # the number of customer arrivals per minute
service_rate =  2.0  # the number of customers served per minute
sim_length =  100000  # how many customers to simulate


def calculate_sample_time(x):
    '''
    Obtain a random number under the simulation assumptions.
    The variable x represents a rate.

    Preconditions:
        x: the rate parameter governing the samples
    Postconditions:
        none
    Return: a floating point number
    '''
    # sample from the exponential distribution, as is common
    # for queueing theory.  Sample values are frequently close to 1/x,
    # occasionally larger, very infrequently very large.
    return rand.expovariate(x)


# customers wait in a service queue
service_queue = Queue.create()

# we're interested in the average time customers wait in the queue
waiting = Statistics.create()
data = []

# keep track of when a new customer will appear
nextArrival = calculate_sample_time(arrival_rate)

# keep track of when a customer can be served
nextService = nextArrival + calculate_sample_time(service_rate)

# simulate the arrival-service
for i in range(sim_length):

    # new customers may arrive while a customer is being served
    while nextArrival < nextService:
        Container.add(service_queue, nextArrival)
        nextArrival = nextArrival + calculate_sample_time(arrival_rate)

    # serve the first customer in the queue
    now_serving = Container.remove(service_queue)

    # how long was the customer waiting?
    wait = nextService - now_serving
    Statistics.add(waiting, wait)
    data.append(wait)

    # determine when service to the current customer will end
    if Container.is_empty(service_queue):
        nextService = nextArrival + calculate_sample_time(service_rate)
    else:
        nextService = nextService + calculate_sample_time(service_rate)


print('Wait time statistics: ', end="")
Statistics.report(waiting)
