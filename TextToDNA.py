'''
textToDNA.py
Dustin Michels
3 March 2017
'''

def convertTextStringToDnaString(messageString):
    dnaString = ""

    for ch in messageString:

        '''
        # check that number is ascii
        try:
            messageString.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError("Perhaps you are entering non-ascii characters? Right now, this tool only deals"
                             " with ascii (American standard) characters.")
         '''

        num = ord(ch)
        print(num)
        print(bin(num))

        for i in range(0, 4):
            res = (num >> i*2) & 0b11
            print(res)
            if res == 0:
                dnaString += 'A'
            elif res == 1:
                dnaString += 'C'
            elif res == 2:
                dnaString += 'G'
            elif res == 3:
                dnaString += 'T'
            else:
                raise ValueError("Seems like an issue with manipulating the binary representation of your characters.")

    return dnaString

'''
def transcribeDNAtoRNA(seqDNA):
    seqRNA = seqDNA[:]
    for i in range(0,len(seqDNA)):
        if seqDNA[i] == 'T':
            seqRNA[i] = 'U'
    return seqRNA
'''

def getDNA(messageString):
    '''
    Main method that will get called by api
    :param messageString:
    :return: dnaString (message encoded in genetic code.)
    '''
    dnaString = convertTextStringToDnaString(messageString)
    return dnaString