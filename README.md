# dnaEncoder
Python programs for encoding text as a DNA sequence (A,C,T,G) or decoding DNA back into text.

## Usage

**To encode text as DNA, you can enter text into the command line, or provide a file.**

To type input:
```bash
python3 textToDNA.py -i
```
To read text from .txt file:
```bash
python3 textToDNA.py -f filename.txt
```

**To decode DNA to text, you have the same options.**

To type input:
```bash
python3 dnaToText.py -i
```
To read text from .txt file:
```bash
python3 dnaToText.py -f filename.txt
```

## Example

```bash
python3 textToDNA.py -f hamlet.txt
```
(This will encode Hamlet as DNA, and save file as DNA_output.txt)

```bash
python3 dnaToText.py -f DNA_outut.txt
```

(This will decode Hamlet back to text, and save as message_output.txt)

## How it Works

The encoding is based on the ASCII / utf-8 code for each character.

  1. A character is converted to its ascii code
  2. The ascii code is examined in its binary form
  3. The binary value is examined two bits at a time, right to left.
    * Two bits can represent 4 digits (0,1,2,3). We set 0-A, 1-C, 2-G, 3-T
    * We look at the LS bits first, and move left across the eight bit representation of a char
    * An eight bit char gets encoded as 4 DNA base pairs (A,C,G, and T).
  
  For example:
  >  * 'd' = 100 in ASCII encoding
  >  * 100 = 0b01100100 in binary
  >  * 00 = A, 01 = C, 10 = G, 01 = C
  >  * 'd' = 0b01100100 = ACGC)
  
 
