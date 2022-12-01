"""
api.py
Dustin Michels
3 March 2017
"""

import sys
import flask
from flask import render_template, request
import dna_to_text
import text_to_dna

app = flask.Flask(__name__)


@app.route("/")
def get_main_page():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/textToDNA/")
def textToDNA():
    # get args from url
    argsMultiDict = request.args
    argsDict = argsMultiDict.to_dict()
    text = argsDict["inputString"]

    try:
        dna = text_to_dna.get_dna(text)
    except ValueError as e:
        return_str = "Error! Can't convert that text into DNA.\n\n" + str(e)
        return return_str

    return dna


@app.route("/dnaToText/")
def dnaToText():
    # get args from url
    args_multi_dict = request.args
    args_dict = args_multi_dict.to_dict()
    dna = args_dict["inputString"]

    try:
        message = dna_to_text.get_message(dna)
    except ValueError:
        return "Error! That might not be valid DNA."

    return message


if __name__ == "__main__":
    """
    Example usage: 'python3 api.py localhost 5000'
    """

    if len(sys.argv) != 3:
        print("Usage: {0} host port".format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
