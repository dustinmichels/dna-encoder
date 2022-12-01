"""
textToDNA.py
Dustin Michels
3 March 2017
"""


def text_string_to_dna_string(message_string):
    dna_string = ""

    for ch in message_string:

        """
        # check that number is ascii
        try:
            message_string.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError("Perhaps you are entering non-ascii characters? Right now, this tool only deals"
                             " with ascii (American standard) characters.")
        """

        num = ord(ch)
        print(num)
        print(bin(num))

        for i in range(0, 4):
            res = (num >> i * 2) & 0b11
            print(res)
            if res == 0:
                dna_string += "A"
            elif res == 1:
                dna_string += "C"
            elif res == 2:
                dna_string += "G"
            elif res == 3:
                dna_string += "T"
            else:
                raise ValueError(
                    "Seems like an issue with manipulating the binary representation of your characters."
                )

    return dna_string


"""
def transcribeDNAtoRNA(seqDNA):
    seqRNA = seqDNA[:]
    for i in range(0,len(seqDNA)):
        if seqDNA[i] == 'T':
            seqRNA[i] = 'U'
    return seqRNA
"""


def get_dna(message_string):
    """
    Main method that will get called by api
    :param message_string:
    :return: dnaString (message encoded in genetic code.)
    """
    dna_string = text_string_to_dna_string(message_string)
    return dna_string
