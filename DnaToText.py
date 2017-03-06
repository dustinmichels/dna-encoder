'''
dnaToText.py
Dustin Michels
3 March 2017
'''
def makeStringDNAIntoArray(dnaString):
    dnaArray =[]
    for ch in dnaString:
        dnaArray.append(ch)
    return dnaArray

def dnaArrayToTextString(dnaArray):
    message = ""
    byteString = ""
    byteCounter = 0
    byteCoutnerReachedEight = False
    returnStringOnlyHasNullChs = True

    for nucleotide in range(0,len(dnaArray)):

        # Start building binary string based on base pair values
        if (dnaArray[nucleotide] == 'a'):
            byteString = "00" + byteString
        elif (dnaArray[nucleotide] == 'c'):
            byteString = "01" + byteString
        elif (dnaArray[nucleotide] == 'g'):
            byteString = "10" + byteString
        elif (dnaArray[nucleotide] == 't'):
            byteString = "11" + byteString
        else:
            raise ValueError("Non-nucleotide input. Input could not be converted to binary")

        # When string is 8 bits long, convert to int, then ASCII char
        # Add that char to "message"
        byteCounter = byteCounter + 2
        if (byteCounter == 8):
            charVal = int(byteString, 2)
            messageAddition = chr(charVal)

            # No fun to only return "Null" character (coded by 4 As in a row)
            if messageAddition != "\x00":
                returnStringOnlyHasNullChs = False

            message += messageAddition
            byteString = ""
            byteCounter = 0
            byteCoutnerReachedEight = True

    if (byteCoutnerReachedEight):
        if returnStringOnlyHasNullChs:
            return "Null!\n\n(Note: Four As in a row translate into the 'null' character!)"
        else:
            return message
    else:
        return "Too short! It takes at least 4 nucleotides to make a character"

def getMessage(dnaString):

    if isinstance(dnaString, str):
        dnaString = dnaString.lower() # make lowercase
        dnaArray = makeStringDNAIntoArray(dnaString)
        messageString = dnaArrayToTextString(dnaArray)
    else:
        raise ValueError("Input is not a string")

    print(messageString)
    return messageString