# CMPT 145: Broken program for debugging
# Sorry, the programmer did not provide any documentation.

def get_data(n): #data param unnecessary
    """
    Purpose: Takes in a number n and asks the user n times for an integer. Each
             integer is appended to a list and returned.
    Pre-condition:
        :param n: an integer representing the number of integers to ask from
                  the user
    Post-condition: None
    return: a list of the numbers that was input by the user
    """
    data = []
    for i in range(n):
        #console input MUST be greater than zero
        data.append(int(input('Enter one integer only:')))
    return data

def find_min_and_max(data): #2 param unnecessary
    """
    Purpose: Takes in a list of integers and get the smallest and largest
             integers in the list
    Pre-condition:
        :param data: a list of integers
    Post-condition: None
    Return: the_min the smallest number in the list
            the_max the largest number in the list

    """
    the_min = min(data)
    the_max = max(data)
    return the_min, the_max

def counting(data):
    """
    Purpose: Counts the amount of time that a number appears in a list
             of integers
    Pre-condition:
        :param data: a list of integers
    Post-condition: None
    Return: a list of integers, each number represents the number of times the
            index number appeared in the input list
    """
    the_min = 0
    the_max = 0
    the_min, the_max = find_min_and_max(data)

    fsize = the_min + the_max
    frequency = [0]*fsize

    #this for loop will break if any element in data is less than 1
    for d in data:
        j = d - the_min + 1
        frequency[j] += 1

    return frequency


def draw_histogram(frequency):
    """
    Purpose: Prints a histogram.
    Pre-condition:
        :param frequency: A list of numbers where each element is the number of
                          times a '*' should be printed beside the index number
    Post-condition: None
    Return: None
    """
    print("\n\n\n ----------- Histogram ----------------\n")

    for index, f in enumerate(frequency[1:]):
        print(index + 1, '*'*f)


data_size = int(input('How many data values?'))
data = get_data(data_size)
frequency = counting(data)
draw_histogram(frequency)
