# Some simplified code for the lectures on Huffman Coding


class HuffmanTree(object):

    def __init__(self,freq=0,char=None,left=None,right=None):
        """
        Purpose:
            Initializes the HuffmanTree object.
            To create a leaf node
                aleaf = HuffmanTree(freq=10, char='A')
                bleaf = HuffmanTree(freq=15, char='E')
            To create an internal node:
                node = HuffmanTree(left=aleaf,right=bleaf)
        Pre-conditions:
            :param freq: a positive integer
            :param char: a character
            :param left: another HuffmanTree
            :param right: another HuffmanTree
        """
        self.char = char
        self.left = left
        self.right = right

        if left is None and right is None:
            self.freq = freq
        else:
            self.freq = left.freq + right.freq




def build_huffman(freq_list):
    """
    Purpose:
        Build a HuffmanTree from the frequency list.
    Pre-conditions:
        freq_list: A list of (character,frequency) pairs.
    Return:
        A HuffmanTree
    """
    # create a list of Huffman leafs
    trees = [HuffmanTree(freq=f,char=c) for c,f in freq_list]

    # keep merging until there's one tree
    while len(trees) > 1:
        # take the two lowest frequency trees
        t1 = delete_min(trees)
        t2 = delete_min(trees)
        # merge them, and put them back
        trees.append(HuffmanTree(left=t1, right=t2))

    return trees[0]



def build_codec(htree):
    """
    Purpose:
        Build a dictionary of char-code pairs from the tree.
    Return:
        :return: a dictionary mapping character to code
    """
    codec = {}
    def encoder(tree, code):
        """
        A traversal to construct the codes recursively.
        Pre-conditions:
            :param tree: A Huffman tree
            :param code: A string that represents the code
        Post-conditions:
            Adds a code to the dictionary codec at every leaf.
        """
        if is_leaf(tree):
            codec[tree.char] = code
        else:
            encoder(tree.left,  code+'0')
            encoder(tree.right, code+'1')

    if is_leaf(htree):
        # special case: message contains only one character
        codec[htree.char] = '0'
    else:
        encoder(htree, '')
    return codec


def encode(strings, codec):
    """
    Purpose:
        Use the codec to encode the strings.
    Pre-conditions:
        strings: A list of strings to encode.
        codec: A dictionary mapping characters to codes
    Return:
        a list of encoded strings
    """
    output = []

    # encode the message
    for s in strings:
        encoded = []
        for char in s:
            encoded.append(codec[char])
        output.append(''.join(encoded))

    return output




def to_string(codec):
    """
    Purpose:
        Represents the codec as a list of strings for inclusion in 
        an output file.  Each string has the code first, a colon ':'
        and then a character in single quotes.  E.g. "01:'b'"  
    Pre-conditions:
        codec: a dictionary mapping characters to binary sequences.
    Return:
        A list of strings.
    """
    output = []
    # construct the codec for output
    for char in codec:
        output.append(codec[char] + ':' + "'" + char + "'")
    return output

def decode(coded_message, codec):
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
            # the slice between first and last is a code
            decoded_chars.append(codec[partial_code])
            first = last
            last  = first + 1
        else:
            # the slice is not a code, so increase the size
            last += 1
    return ''.join(decoded_chars)


def count_characters(contents):
    """
    Purpose:
        Count the characters in the contents.
    Pre-conditions:
        :param contents: a list of strings.
    Return:
        :return: a list of (character,frequency) tuples
    """
    freqs = dict()
    for line in contents:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
    return list(freqs.items())


def delete_min(trees):
    """
    Purpose:
        Find and delete the tree in trees with the minimum frequency.
    Pre-conditions:
        trees: a list of HuffmanTree objects
    Post_conditions:
        The tree with the minimum value is removed from the list.
    Return:
        The tree with the minimum value.
    """
    min_i = 0
    min_tree = trees[min_i]
    for i in range(1,len(trees)):
        atree = trees[i]
        if atree.freq < min_tree.freq:
            min_i = i
    return trees.pop(min_i)

def is_leaf(htree):
    """
    Purpose:
        Check if the given HuffmanTree is a leaf.
    Pre-conditions:
        htree: a HuffmanTree object
    Return:
        True if the given tree is a leaf.
    """
    return htree.left is None and htree.right is None
    
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

def build_decoder_from_encoder(encoder):
    """
    Purpose:
        Construct a dictionary mapping from binary
        sequences to characters.
    Pre-conditions:
        encoder: a dictionary mapping from characters 
        to binary sequences.
    Return:
        A dictionary.
    """
    decoder = dict()
    for c in encoder:
        decoder[encoder[c]] = c
    return decoder

def build_decoder_from_strings(pairs):
    """
    Purpose:
        Construct a dictionary mapping from binary
        sequences to characters.
    Pre-conditions:
        pairs: a list of strings that represent 
        the decoder mapping, as produced by to_string()
    Return:
        A dictionary.
    """
    # Each string has a special layout, e.g,  "0101:'c'"
    # the binary sequence ends at the colon, which is 4
    # characters before the end of the string.
    codec = dict()
    for p in pairs:
        codelen = len(p) - 4
        char = p[codelen+2]
        code = p[:codelen]        
        codec[code] = char
    return codec
        
if __name__ == '__main__':
    message = ['To be, or not to be,', 
               'That is the question.']
    print('Original:', message)

    freqs = count_characters(message)
    ht = build_huffman(freqs)
    codec = build_codec(ht)
    compressed = encode(message, codec)
    print('Encoded :', compressed)
    rev_codec1 = build_decoder_from_encoder(codec)
    inflated = [decode(c, rev_codec1) for c in compressed]
    print('Decoded :', inflated)
    codescr = to_string(codec)
    print('Codec   :', codescr)
    rev_codec2 = build_decoder_from_strings(codescr)
    inflated2 = [decode(c, rev_codec2) for c in compressed]
    print('Decoded :', inflated2)
    
    message_bits = sum([8*len(s) for s in message])
    compressed_bits = sum(len(s) for s in compressed)
    ratio = compressed_bits / message_bits
    print('Compression ratio:', ratio)

