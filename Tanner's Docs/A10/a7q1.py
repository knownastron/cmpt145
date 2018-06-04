# CMPT 145: Assignment 7 Question 1
# Design, Testing, Defensive Programming, and Style

import sys as sys


def main():
    """
    Purpose:
        Application to read a file, count characters,
        and display the top 10 most frequently occurring
        characters.
    :return: None
    """
    # Read a text file
    # Count the character frequencies
    # Display the top 10 most frequent used characters
    assert len(sys.argv) == 2, 'No filename given'
    fname = sys.argv[1]
    lines = read_file(fname)
    freqs = count_characters(lines)
    display_top(freqs, 10)


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
    return lines


def count_characters(contents):
    """
    Purpose:
        Count the characters in the contents.
    Pre-conditions:
        :param contents: a list of strings.
    Return:
        :return: a dictionary with the characters and frequencies
    """
    freqs = dict()
    for line in contents:
        for c in line:
            if c in freqs:
                freqs[c] += 1
            else:
                freqs[c] = 1
    return freqs


def display_top(frequencies, k):
    """
    Purpose:
        Display the top k most frequently occuring keys.
    :param frequencies: a dictionary of keys and counts.
    :param k: an integer, k >= 0
    :return:
    """

    def comp(p):
        return p[1]

    assert k >= 0, 'Must have non-negative ordinal'

    pairs = [(c, frequencies[c]) for c in frequencies]
    pairs.sort(key=comp, reverse=True)
    for c, v in pairs[:k]:
        print("'" + c + "'", v)


if __name__ == '__main__':
    main()
