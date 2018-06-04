#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import sys

def get_confession(file_name):
    """
    Purpose:
        Takes in the name of the file, opens the file, reads each line, creates a list of lists of characters
    Pre-Condition:
        :param file_name: string that is the name of the file, ending in .txt
    Post-Condition:
        None
    Return:
        A list of lists where each element is a character from the document that was opened
    """

    file = open(file_name, "r")
    line = file.readline().rstrip().split()
    confession = []

    while line:
        confession.append(line)
        line = file.readline().rstrip().split()

    return confession


def find_word(confession, word):
    """
    Purpose: find if the desired word is found orthogonally in the list of characters
    Pre-condition:
        :param confession: a list of lists where each element is a character
        :param word: a string in capital letters that is to be searched for in param confession
    Post-condition: None.
    Return:
        True if the crime string appears orthogonally in the confessions input of characters
        False if the crime string does not appear orthogonally in the
    """

    reverse_word = word[::-1]

    #check horizontal
    for y in range(len(confession)):
        line = "".join(confession[y])
        if word in line or reverse_word in line:
            return True

    #check vertical
    for x in range(len(confession[0])):
        line = ""
        for y in range(len(confession)):
            line += confession[y][x]
        if word in line or reverse_word in line:
            return True

    return False


def print_is_guilty(verdict, word):
    """
        Purpose:
            prints the statement that ""Gentleman GoGo IS GUILTY of <word_to_look_for>" or
            "word_to_look_for> was NOT found"
        Pre-condition:
            :param verdict: a boolean
            :param word: a string in capital letters that is to be searched for in param confession
        Post-condition:
            None
        Return:
            None
    """
    if verdict:
        print("Gentleman GoGo IS GUILTY OF", word)
    else:
        print(word, "was NOT found")



#runs the program if there are enough command line arguments
if len(sys.argv) == 3:
    file_name = sys.argv[1]
    word_to_look_for = sys.argv[2].upper()
    confession = get_confession(file_name)
    verdict = find_word(confession, word_to_look_for)
    print_is_guilty(verdict, word_to_look_for)
