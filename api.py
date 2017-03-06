'''
api.py
Dustin Michels
3 March 2017
'''
import sys
import flask
from flask import render_template, request
import DnaToText
import TextToDNA

app = flask.Flask(__name__)

@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/textToDNA/')
def textToDNA():
    # get args from url
    argsMultiDict = request.args
    argsDict = argsMultiDict.to_dict()
    text = argsDict["inputString"]

    try:
        dna = TextToDNA.getDNA(text)
    except ValueError as e:
        returnStr = "Error! Can't convert that text into DNA.\n\n" + str(e)
        return returnStr

    return dna

@app.route('/dnaToText/')
def dnaToText():
    # get args from url
    argsMultiDict = request.args
    argsDict = argsMultiDict.to_dict()
    dna = argsDict["inputString"]

    try:
        message = DnaToText.getMessage(dna)
    except ValueError:
        return "Error! That might not be valid DNA."

    return message


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)