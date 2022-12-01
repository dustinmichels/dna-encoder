# dna encoder

A Flask web application that encodes text as DNA. This is a not-terribly-useful project,
intended mainly to be an educational resource for users and developers alike to explore
the similarities and differences in how information is encoded in computers (in binary digits)
versus in organisms (in a series of nucleotide base pairs, called DNA.).

## How it works

See http://dnaencoder.dustinmichels.com/about/

## What's Inside

- The file `api.py` uses Flask to interact with web
- The templates/ folder contains `.html` files and the static/ folder holds `.css`, `.js`,
  and image files.
- `TextToDna.py` is used to encode text as a DNA sequence of As,Ts,Cs,and Gs.
- `DnaToText.py` is used to decode a DNA sequence back into text.
