import json
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.english_to_french(textToTranslate)   # calling the english to french translation function
    return frenchText

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.french_to_english(textToTranslate) # calling the french  to english translation function
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template("index.html") # the code to render the default dislay page      
       
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
