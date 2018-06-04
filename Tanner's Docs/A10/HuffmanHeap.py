# CMPT 145: Huffman Heap
# Algorithms: Huffman Coding


class HuffmanHeap(object):
    def __init__(self, leafs):
        """
        Initialize the queue.  The list leafs must be sorted!
        """
        self.__leafs = leafs
        self.__queue = []

    def enqueue(self, tree):
        """
        Put the tree in the queue
        """
        self.__queue.append(tree)

    def dequeue(self):
        """
        Return the smallest value in the queue.
        Note: this implementation assumes elements
        can be compared using less-than <
        """
        if len(self.__leafs) == 0:
            return self.__queue.pop(0)
        elif len(self.__queue) == 0:
            return self.__leafs.pop(0)
        elif self.__leafs[0] < self.__queue[0]:
            return self.__leafs.pop(0)
        else:
            return self.__queue.pop(0)

    def __len__(self):
        """
        Return the number of data values stored in the queue.
        """
        return len(self.__leafs) + len(self.__queue)

    def display(self):
        """
        Display the data for debugging.
        """
        print('leafs:', self.__leafs)
        print('new:', self.__queue)


if __name__ == '__main__':
    # a demo assuming the elements will be numbers.
    hq = HuffmanHeap([1, 1, 2, 3, 4, 5, 6, 6, 10, 15, 20])
    hq.display()
    while len(hq) > 1:
        v1 = hq.dequeue()
        v2 = hq.dequeue()
        hq.enqueue(v1 + v2)
        hq.display()
    print('Done!')
