# CMPT 145: Assignment 8 Question 2
#

import sys as sys
import Huffman as HT
import HuffmanHeap as HH

DEFAULT_OUTPUT_FILE = 'encoded.txt'

def main():
    """
    Purpose:
        Application to read and encode a file using Huffman codes.
        Usage: python3 Encoder.py <filename>
        Sends output to DEFAULT_OUTPUT_FILE
    Return:
        :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3', sys.argv[0], '<filename>')
        print('-- sends output to', DEFAULT_OUTPUT_FILE, '-- ')
        return

    fname = sys.argv[1]
    lines = read_file(fname)
    freqs = count_characters(lines)
    codec = build_codec(freqs)
    coded = encode(lines, codec)
    write_file(DEFAULT_OUTPUT_FILE, coded)


def read_file(fname):
    """
    Purpose:
        Read a file and return contents in a list of strings.
    Preconditions:
        :param fname: the name of a text file
    Return:
        :return: a list of strings, one string for each line
    """
    tfile = open(fname)
    lines = [l.rstrip() for l in tfile]
    tfile.close()
    return lines


def write_file(fname, lines):
    """
    Purpose:
        Write the data in lines to the named file.
        Warning: this will over-write any data in the named file!
    Preconditions:
        :param fname: the name of a text file
        :param lines: a list of strings
    Post-condition:
        The named file is created or over-written.
    Return:
        :return: None
    """
    tfile = open(fname, 'w')
    for line in lines:
        tfile.write(line + '\n')
    tfile.close()


def count_characters(contents):
    """
    Purpose:
        Count the characters in the contents.
    Pre-conditions:
        :param contents: a list of strings.
    Return:
        :return: a list of the character-frequency pairs
    """
    freqs = dict()
    for line in contents:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
    return list(freqs.items())


def build_codec(freq_list):
    """
    Purpose:
        Build a dictionary containing character:code pairs from 
        the frequency list.
    Pre-conditions:
        :param freq_list: A list of (character,frequency) pairs.
    Return:
        :return: a dictionary
    """
    # sort the frequency list
    freq_list.sort(key=lambda p: p[1])
    
    # create the queue of Huffman trees
    # note: a new ADT for this purpose!
    hq = HH.HuffmanHeap(
            [HT.HuffmanTree(freq=f, char=c) for c, f in freq_list]
            )
    
    # dequeue 2 trees, combine them, and enqueue the resulting tree
    while len(hq) > 1:
        t1 = hq.dequeue()
        t2 = hq.dequeue()
        hq.enqueue(HT.HuffmanTree(left=t1, right=t2))
    
    #build a codec from the only tree that's left
    survivor = hq.dequeue()
    return survivor.build_codec()


def encode(strings, codec):
    """
    Purpose:
        Use the codec to create the data to be sent to the output file.
    Pre-conditions:
        :param strings: A list of strings to encode.
        :param codec: A dictionary containing character-code pairs
    Return:
        :return: a list of strings including:
            the number of codes the number of coded lines,
            the codes
            the coded lines
    """
    output = []
    output.append(str(len(codec)) + ' ' + str(len(strings)))
    for char in codec:
        output.append(codec[char] + ':' + "'" + char + "'")
    for s in strings:
        encoded = []
        for char in s:
            encoded.append(codec[char])
        output.append(''.join(encoded))
    return output


if __name__ == '__main__':
    main()
