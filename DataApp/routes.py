from DataApp import app
import json, plotly
from flask import render_template
from Data.Wrangling import data_wrangle 


@app.route('/')
@app.route('/index')

def index():

    figures,topO,total,topD = data_wrangle()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    print("\n",ids)
    print("\n", figuresJSON)

    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON,
                           top_origin = topO,
                           total = total,
                           top_destination = topD )