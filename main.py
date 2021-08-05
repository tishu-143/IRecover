from datetime import date
from flask import Flask, render_template, request
from prediction import predictTheSeverity
import pandas as pd

app = Flask(__name__)


@app.route("/checkForSeverity")
def homePage():
    #requestData = request.json
    df = predictTheSeverity()
    return df.to_json(orient='records')



if __name__ == '__main__':
    app.run()