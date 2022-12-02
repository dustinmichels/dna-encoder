# dna encoder

A Flask web application that encodes text as DNA.

This is a not-terribly-useful project, for exploring the similarities and differences in how information is encoded in computers (in binary digits) vs. in organisms (in a series of nucleotide base pairs, called DNA.).

_I made in in 2017. Minor updates (for deployment) in 2022._

## Setup

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the app:

```sh
flask --app main run
```

Deploy to [Deta](https://docs.deta.sh/docs/micros/about/):

```sh
deta deploy
```

## How it works

See: http://dnaencoder.dustinmichels.com/about/

## What's Inside

- The file `main.py` uses Flask to interact with web
- `text_to_dna.py` is used to encode text as a DNA sequence of As,Ts,Cs,and Gs.
- `dna_to_text.py` is used to decode a DNA sequence back into text.
- The `templates/` folder contains jinja2 template `.html` files
- The `static/` folder holds `.css`, `.js`, and image files.
