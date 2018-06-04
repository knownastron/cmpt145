# CMPT 145: Broken program for debugging
# Sorry, the programmer did not provide any documentation.

def get_data(n, data):
    data = []
    for i in range(n):
        data.append(input('Enter one integer only:'))


def find_min_and_max(data, the_min, the_max):
    the_min = min(data)
    the_max = max(data)


def counting(data):
    the_min = 0
    the_max = 0
    find_min_and_max(data, the_min, the_max)

    fsize = the_min + the_max
    frequency = [0]*fsize

    for d in data:
        j = d - the_min + 1
        frequency[j] += 1

    return frequency


def draw_histogram(frequency, the_min, the_max):
    print("\n\n\n ----------- Histogram ----------------\n")

    for f in frequency:
        print(f, '*'*f)


data_size = int(input('How many data values?'))
data = get_data(data_size, [])
frequency = counting(data)
draw_histogram(frequency,0,0)
