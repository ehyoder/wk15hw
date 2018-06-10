import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)
Base = automap_base()

# Connect to Engine
engine = create_engine("sqlite:///db/belly_button_biodiversity.sqlite",echo=False)
conn = engine.connect()
# Reflect the tables 
Base.prepare(engine, reflect=True)

# Create variables for tables
Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_metadata = Base.classes.samples_metadata

session = Session(engine)

#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    """Return to the dashboard homepage."""
    return render_template("index.html")

@app.route("/names")
def sample_names():
    """Return a list of sample names"""
    
    # query for sample names
@app.route('/names')
def names():
    """Return a list of sample names"""

    # query with pandas
    names_results = session.query(Samples).statement
    names_results_df = pd.read_sql_query(names_results, session.bind)
    names_results_df.set_index('otu_id', inplace=True)

    # return a list of the sample names 
    return jsonify(list(names_results_df.columns))

@app.route("/otu")
def otu_data():
    results = session.query(Otu.lowest_taxonomic_unit_found).all()

    # use numpy ravel to get a 1D array
    otu_list = list(np.ravel(results))
    return jsonify(otu_list)

@app.route("/metadata/<sample>")

def sample_metadata(sample):
    """Return a json dictionary of sample metadata"""
    sample_list = [Samples_metadata.SAMPLEID, Samples_metadata.ETHNICITY,
           Samples_metadata.GENDER, Samples_metadata.AGE,
           Samples_metadata.LOCATION, Samples_metadata.BBTYPE]

    # query for all sample list items
    results = session.query(*sample_list).all()

    # create a dictionary of metadata information
    sample_metadata = {}
    for result in results:
        sample_metadata['SAMPLEID'] = result[0]
        sample_metadata['ETHNICITY'] = result[1]
        sample_metadata['GENDER'] = result[2]
        sample_metadata['AGE'] = result[3]
        sample_metadata['LOCATION'] = result[4]
        sample_metadata['BBTYPE'] = result[5]

    return jsonify(sample_metadata)

@app.route("/wfreq/<sample>")
def sample_washing_frequency(sample):
    """Return the Weekly Washing Frequency as a number."""

    # query for washing frequency
    results = session.query(Samples_metadata.WFREQ).\
        filter(Samples_metadata.SAMPLEID == sample[3:]).all()
    # get results as a 1D array
    wfreq = np.ravel(results)

    # return the number of washes
    return jsonify(int(wfreq))


#     # Format the data for Plotly
#     plot_trace = {
#             "x": df["--"].values.tolist(),
#             "y": df["--"].values.tolist(),
#             "type": "--"
#     }
#     return jsonify(plot_trace)

#@app.route("/samples/<sample>")
#def sample_values():
    #"""Returns a list of dictionaries containing sorted lists for 'otu_ids' and 'sample_values'"""

#     # query for list of dictionaries

#     # Format the data for Plotly
#     plot_trace = {
#             "x": df["--"].values.tolist(),
#             "y": df["--"].values.tolist(),
#             "type": "--"
#     }
#     return jsonify(plot_trace)

if __name__ == '__main__':
    app.run(debug=True)
