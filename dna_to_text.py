"""
dnaToText.py
Dustin Michels
3 March 2017
"""


def string_dna_to_array(dna_string):
    dna_array = []
    for ch in dna_string:
        dna_array.append(ch)
    return dna_array


def dna_array_to_text_string(dna_array):
    message = ""
    byte_string = ""
    byte_counter = 0
    byte_counter_reached_eight = False
    return_string_only_has_null_chs = True

    for nucleotide in range(0, len(dna_array)):

        # Start building binary string based on base pair values
        if dna_array[nucleotide] == 'a':
            byte_string = "00" + byte_string
        elif dna_array[nucleotide] == 'c':
            byte_string = "01" + byte_string
        elif dna_array[nucleotide] == 'g':
            byte_string = "10" + byte_string
        elif dna_array[nucleotide] == 't':
            byte_string = "11" + byte_string
        else:
            raise ValueError("Non-nucleotide input. Input could not be converted to binary")

        # When string is 8 bits long, convert to int, then ASCII char
        # Add that char to "message"
        byte_counter = byte_counter + 2
        if byte_counter == 8:
            char_val = int(byte_string, 2)
            message_addition = chr(char_val)

            # No fun to only return "Null" character (coded by 4 As in a row)
            if message_addition != "\x00":
                return_string_only_has_null_chs = False

            message += message_addition
            byte_string = ""
            byte_counter = 0
            byte_counter_reached_eight = True

    if byte_counter_reached_eight:
        if return_string_only_has_null_chs:
            return "Null!\n\n(Note: Four As in a row translate into the 'null' character!)"
        else:
            return message
    else:
        return "Too short! It takes at least 4 nucleotides to make a character"


def get_message(dna_string):
    if isinstance(dna_string, str):
        dna_string = dna_string.lower()  # make lowercase
        dna_array = string_dna_to_array(dna_string)
        message_string = dna_array_to_text_string(dna_array)
    else:
        raise ValueError("Input is not a string")

    print(message_string)
    return message_string
