# CMPT 145: Lists, references
# Histograms!


def get_data(n):
    """Grab n integers from the console.  
    Return them in a list.
    """
    data = []
    for i in range(n):
        data.append(int(input('Enter one integer only:')))
    return data

def find_min_and_max(data):
    """ Input: a list of data values 
        Return: a tuple containing the min and max
    """
    the_min = min(data)
    the_max = max(data)
    return the_min, the_max


def counting(data, the_min, the_max):
    """ Count the data values in the data.
        Input: a list of data values (integers!)
               the min and max values in the data
        Returns a list of counts for all the data values.
        Note: the frequency list uses index 0 for the min
    """
    
    # how big does the freqwuency list have to be?
    fsize = the_max - the_min + 1
    frequency = [0]*fsize

    # count the data values
    for d in data:
        # the min data value is stored at index zero
        index = d - the_min
        frequency[index] += 1

    return frequency


def draw_histogram(frequency, the_min):
    """ Display a lame histogram on the console.
        Input: a frequency list
               the min value in the data
    """
    print("\n\n\n ----------- Histogram ----------------\n")

    # frequency stores counts, but not data values
    # so at index 0, we have the min data value

    for f in range(len(frequency)):
        print(f+the_min, '*'*frequency[f])

# main script
data_size = int(input('How many data values?'))
data = get_data(data_size)
the_min, the_max = find_min_and_max(data)
frequency = counting(data, the_min, the_max)
draw_histogram(frequency, the_min)

