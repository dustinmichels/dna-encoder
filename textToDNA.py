'''
textToDNA.py
Dustin Michels
24 Jan 2017
'''
import sys

def seqToString(seq):
    res = ""
    for i in range(0,len(seq)):
        res += (seq[i])
    return res

def printSeqWithDashes(seq):
    res = ""
    for i in range(0,len(seq)):
        count = i+1
        isThird = count%3
        res += (seq[i])
        if ((isThird == 0) and (i !=(len(seq)-1))):
            res += "-"
    print(res)

def convertTextToDNA(message, seqDNA):
    for ch in message:
        num = ord(ch)
        for i in range (0,4):
            res = (num >> i*2) & 0b11
            if res == 0:
                seqDNA.append('A')
            elif res == 1:
                seqDNA.append('C')
            elif res == 2:
                seqDNA.append('G')
            elif res == 3:
                seqDNA.append('T')
            else:
                print("Error! Binary could not be converted to ACGT")
                exit()
    return seqDNA

def transcribeDNAtoRNA(seqDNA):
    seqRNA = seqDNA[:]
    for i in range(0,len(seqDNA)):
        if seqDNA[i] == 'T':
            seqRNA[i] = 'U'
    return seqRNA

def main():

    seqDNA = []
    seqRNA = []

    def usageMSG():
        print("USAGE:")
        print(">python3 textToDNA.py -i [to type input]")
        print(">python3 textToDNA.py -f filename [to read text from .txt file]")
        exit(0)

    # logic for running program based on command line call
    # python3 textToDNA.py -i  -> get text from user input
    # python3 textToDNA.py -f filename -> get text from file "filename"
    if (len(sys.argv) < 2):
        usageMSG()
    if (sys.argv[1] == '-i'):
        message = input("Enter a message: ")
    elif (sys.argv[1] == '-f'):
        filename = sys.argv[2]
        try:
            f = open(filename, 'r')
        except IOError as e:
            print("File not found!")
            usageMSG()
        message = f.read()
        f.close()
    else:
        usageMSG()

    seqDNA = convertTextToDNA(message, seqDNA)
    seqRNA = transcribeDNAtoRNA(seqDNA)
    DNA_String = seqToString(seqDNA)
    RNA_String = seqToString(seqRNA)

    # write DNA output to file, DNA_output.txt
    f = open("DNA_output.txt", 'w')
    f.write(DNA_String)

    def printToTerminal():
        print("DNA:")
        printSeqWithDashes(seqDNA)
        print("RNA:")
        printSeqWithDashes(seqRNA)

    # logic for getting user input on
    # [1] printing out results? (yes or no) [2] with dashes? (yes or no).
    while(True):
        reply = input("Print out results? [y/n]: ")
        if (reply.lower() == 'y'):
            while(True):
                reply2 = input("Print with dashes to seperate codons? [y/n]: ")
                if (reply2.lower() == 'y'):
                    printToTerminal()
                    break
                elif (reply2.lower() == 'n'):
                    print("DNA:\n" + DNA_String)
                    print("RNA:\n" + RNA_String)
                    break
                else:
                    print("Oops. Try again.")
            print("done.")
            break
        elif (reply.lower() == 'n'):
            print("done.")
            break
        else:
            print("Oops. Try again.")

if __name__ == "__main__":
    main()
