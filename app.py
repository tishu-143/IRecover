from datetime import date
from flask import Flask, render_template, request
from flask_cors.decorator import cross_origin
from prediction import predictTheSeverity
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/checkForSeverity")
@cross_origin()
def homePage():
    requestData = request.json
    df = predictTheSeverity(requestData)
    data = pd.DataFrame(df, columns=['Covid-19'])
    value = data.iloc[0]['Covid-19']
    if value == 0:
        return "Nothing to worry about, proper medication, diet and rest will make you healthy soon."
    else:
        return "It is better that you consult the doctor as soon as possible to be on safe side"



if __name__ == '__main__':
    app.run()