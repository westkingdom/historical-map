import pandas as pd

from libs import globs as gl

###
# Create a dataframe from the CSV file
# Copy that dataframe for later use
# Create a dict from that datframe for iteration
###

def prepdata(cols):
    bigframe = impcsv()
    data = opencsv(bigframe)  # Make a copy of the frame for later use
    cols = listify(data)
    return cols


# Open the CSV file, create a Dataframe, Copy it To use later, return the copy
def impcsv():
    bigframe = pd.read_csv('libs/wkcsv_source.csv', names=gl.colnames, index_col=False, header=0, na_values='.',
                           dtype=str)
    return bigframe


def opencsv(bigframe):
    data = pd.DataFrame.copy(bigframe, deep=True)
    # initialize(data)
    return data


# take DataFrame make a dict
def listify(data):
    cols = gl.cols
    for col in data:
        cols[col] = data[col].tolist()
    return cols
