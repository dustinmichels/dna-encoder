/*
    script.js
    Dustin Michels, 3 March 2017
 */

var DNA_PLACEHOLDER = "ACCCCCGCAGTC...";
var TEXT_PLACEHOLDER = "Text message here...";

function conversionDirIsTextToDNA() {
    var radios = document.getElementsByName('textOrDNA_radio');
    if (radios[0].checked) {
        return true;
    }
    else if (radios[1].checked) {
        return false;
    }
}

function onSelectDirectionOfConversion() {
    if (conversionDirIsTextToDNA()) {
        document.getElementById('text_to_DNA_img').style.display = 'inline';
        document.getElementById('DNA_to_text_img').style.display = 'none';
        document.getElementById('inputTextArea').placeholder = TEXT_PLACEHOLDER;
        document.getElementById('outputTextArea').placeholder = DNA_PLACEHOLDER;
    }
    else {
        document.getElementById('text_to_DNA_img').style.display = 'none';
        document.getElementById('DNA_to_text_img').style.display = 'inline';
        document.getElementById('inputTextArea').placeholder = DNA_PLACEHOLDER;
        document.getElementById('outputTextArea').placeholder = TEXT_PLACEHOLDER;
    }
}

function changeConversionDir() {
    if (conversionDirIsTextToDNA()) {
        document.getElementById('dnaToTextRadio').checked = true;
    }
    else {
        document.getElementById('textToDnaRadio').checked = true;
    }
    onSelectDirectionOfConversion()
}

function doConversion() {

    var inputString = document.getElementById('inputTextArea').value;
    var param = "inputString="+inputString;

    console.log(inputString);
    console.log(param);

    var outputTextArea = document.getElementById('outputTextArea');
    var outString = "";

    if(conversionDirIsTextToDNA()) {
        var url = '/textToDNA';
    }
    else {
        var url = '/dnaToText';
    }

    xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.open('GET', url+"?"+param, true);

    xmlHttpRequest.onreadystatechange = function() {
        if (xmlHttpRequest.readyState == 4 && xmlHttpRequest.status == 200) {
            outString = xmlHttpRequest.response;
            outputTextArea.value = outString
        }
    };
    xmlHttpRequest.send(null)
}

function onClear() {
    document.getElementById('inputTextArea').value = null;
    document.getElementById('outputTextArea').value = null;
}

function onSwap() {
    var outString = document.getElementById('outputTextArea').value;

    document.getElementById('inputTextArea').value = outString;
    document.getElementById('outputTextArea').value = null;

    changeConversionDir();
}

function goToAbout() {
    window.location.href = "/about"
}