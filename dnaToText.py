'''
dnaToText.py
Dustin Michels
1 Feb 2017
'''
import sys

def makeStringDNAIntoArray(stringDNA, seqDNA):
    for ch in stringDNA:
        seqDNA.append(ch)

    return seqDNA

def convertDNAtoText(seqDNA):
    message = ""
    byteString = ""
    byteCounter = 0

    for base in range(0,len(seqDNA)):

        # Start building binary string based on base pair values
        if (seqDNA[base].lower() == 'a'):
            byteString = "00" + byteString
        elif (seqDNA[base].lower() == 'c'):
            byteString = "01" + byteString
        elif (seqDNA[base].lower() == 'g'):
            byteString = "10" + byteString
        elif (seqDNA[base].lower() == 't'):
            byteString = "11" + byteString
        else:
            print("Error! Base pair could not be converted to binary")
            exit()

        # When string is 8 bits long, convert to int, then ASCII char
        # Add that char to "message"
        byteCounter = byteCounter + 2
        if (byteCounter == 8):
            charVal = int(byteString, 2)
            message += chr(charVal)
            byteString = ""
            byteCounter = 0

    return message

def main():

    stringDNA = ""
    seqDNA = []

    def usageMSG():
        print("USAGE:")
        print(">python3 dnaToText.py -i [to type input]")
        print(">python3 dnaToText.py -f filename [to read text from .txt file]")
        exit(0)

    # logic for running program based on command line call
    # python3 dnaToText.py -i  -> get DNA from user input
    # python3 dnaToText.py -f filename -> get DNA from file "filename"
    if (len(sys.argv) < 2):
        usageMSG()
    if (sys.argv[1] == '-i'):
        stringDNA = input("Enter a DNA sequence: ")
    elif (sys.argv[1] == '-f'):
        filename = sys.argv[2]
        try:
            f = open(filename, 'r')
        except IOError as e:
            print("File not found!")
            usageMSG()
        stringDNA = f.read()
        f.close()
    else:
        usageMSG()

    seqDNA = makeStringDNAIntoArray(stringDNA, seqDNA)
    message = convertDNAtoText(seqDNA)

    # write DNA output to file, DNA_output.txt
    f = open("message_output.txt", 'w')
    f.write(message)

    # logic for getting user input on
    # [1] printing out results? (yes or no) [2] with dashes? (yes or no).
    while(True):
        reply = input("Print out results? [y/n]: ")
        if (reply.lower() == 'y'):
            print(message)
            print("done.")
            break
        elif (reply.lower() == 'n'):
            print("done.")
            break
        else:
            print("Oops. Try again.")

if __name__ == "__main__":
    main()
