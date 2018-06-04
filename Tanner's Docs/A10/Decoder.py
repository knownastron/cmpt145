# CMPT 145: Assignment 8 Question 3
#

import sys as sys

DEFAULT_OUTPUT_FILE = '<console>'

def main():
    """
    Purpose
        The main program.
        Usage: python3 Decoder.py <filename>
        Sends output to DEFAULT_OUTPUT_FILE
    Return:
        :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3', sys.argv[0], '<filename>')
        print('-- sends output to', DEFAULT_OUTPUT_FILE, '-- ')
        return

    the_file = open(sys.argv[1])
    assert the_file, 'Could not open file'

    line = the_file.readline().rstrip()
    assert line, 'File had no data'

    sizes = line.split()
    assert len(sizes) == 2, 'First line of file corrupted'

    code_size = int(sizes[0])
    assert code_size > 0, 'Unexpected code size value'

    message_size = int(sizes[1])
    assert message_size > 0, 'Unexpected message size value'

    dc = build_decoder(the_file, code_size)

    for l in range(message_size):
        line = the_file.readline().rstrip()
        message = decode_message(line, dc)
        print(message)

    the_file.close()
    return


def build_decoder(afile, code_size):
    """
    Purpose:
        Build the dictionary by reading some lines from the given file
    Preconditions:
        :param afile: an open file, ready for reading
        :param code_size: the number of lines of code
    Return:
        :return: a dictionary whose keys are 'CODE' and values are <char>
    """
    codec = {}
    for l in range(code_size):
        line = afile.readline().rstrip()
        assert line, 'Expected a code line at line '+str(l)
        cchr = line.split(':')
        code = cchr[0]
        # the normal case: the split created 2 strings
        if len(cchr) == 2:
            char = cchr[1]
        else:
            # if the char is ':' itself, the split will create more than 2
            char = "':'"

        codec[code] = char[1] # The input file has ' ' around the character
    return codec


def decode_message(coded_message, codec):
    """
    Purpose:
        Decode the message using the decoder.
    Preconditions:
        :param coded_message: An encoded string consisting of digits '0' and '1'
        :param codec: a Dictionary of coded_message-character pairs
    Return:
        :return: A string decoded from coded_message
    """
    decoded_chars = []
    first = 0
    last = first + 1
    while first < len(coded_message):
        partial_code = coded_message[first:last]
        if partial_code in codec:
            decoded_chars.append(codec[partial_code])
            first = last
            last = first + 1
        else:
            last += 1
    return ''.join(decoded_chars)



if __name__ == '__main__':
    main()


