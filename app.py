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
    results = db.session.query(Base).all()
    return jsonify(results)

    # Generate the plot trace
    # plot_trace = {
    #    "x": --,
    #     "y": --,
    #     "type": "--"
    # }
    # return jsonify(plot_trace)

#@app.route("/otu")
#def otu_data():
#     plot_trace = {
#             "x": df["--"].values.tolist(),
#             "y": df["--"].values.tolist(),
#             "type": "--"
#     }
#     return jsonify(plot_trace)

@app.route("/metadata/<sample>")
def sample_metadata():
    """Return a json dictionary of sample metadata"""

    # query for json sample metadata
    return jsonify(hello='world')

    # Format the data for Plotly
#     plot_trace = {
#             "x": df["--"].values.tolist(),
#             "y": df["--"].values.tolist(),
#             "type": "--"
#     }
#     return jsonify(plot_trace)

#@app.route("/wfreq/<sample>")
#def sample_washing freqeunce():
    """Return washing frequency as a number"""

#     # query for washing frequency

#     # Format the data for Plotly
#     plot_trace = {
#             "x": df["--"].values.tolist(),
#             "y": df["--"].values.tolist(),
#             "type": "--"
#     }
#     return jsonify(plot_trace)

#@app.route("/samples/<sample>")
#def sample_values():
    """Returns a list of dictionaries containing sorted lists for 'otu_ids' and 'sample_values'"""

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
