import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/--.sqlite"

db = SQLAlchemy(app)


class BB(db.Model):
    __tablename__ = 'bb_data'

    sample_id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String)
    ethnicity = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '?'


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    """Return to the dashboard homepage."""
    return render_template("index.html")

@app.route("/names")
def sample_names():
    """Return a list of sample names"""

    # query for sample names

    # Generate the plot trace
    plot_trace = {
        "x": --,
        "y": --,
        "type": "--"
    }
    return jsonify(plot_trace)


@app.route("/otu")
def otu_data():
    """Return list of OTU descriptions"""

    # query for the otu data

    # Format the data for Plotly
    plot_trace = {
            "x": df["--"].values.tolist(),
            "y": df["--"].values.tolist(),
            "type": "--"
    }
    return jsonify(plot_trace)


@app.route("/metadata/<sample>")
def sample_metadata():
    """Return a json dictionary of sample metadata"""

    # query for json sample metadata
    

    # Format the data for Plotly
    plot_trace = {
            "x": df["--"].values.tolist(),
            "y": df["--"].values.tolist(),
            "type": "--"
    }
    return jsonify(plot_trace)

@app.route("/wfreq/<sample>")
def sample_washing freqeunce():
    """Return washing frequency as a number"""

    # query for washing frequency

    # Format the data for Plotly
    plot_trace = {
            "x": df["--"].values.tolist(),
            "y": df["--"].values.tolist(),
            "type": "--"
    }
    return jsonify(plot_trace)

@app.route("/samples/<sample>")
def sample_values():
    """Returns a list of dictionaries containing sorted lists for 'otu_ids' and 'sample_values'"""

    # query for list of dictionaries

    # Format the data for Plotly
    plot_trace = {
            "x": df["--"].values.tolist(),
            "y": df["--"].values.tolist(),
            "type": "--"
    }
    return jsonify(plot_trace)

if __name__ == '__main__':
    app.run(debug=True)
