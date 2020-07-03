import flask
import lzhw
from time import time
import pandas as pd
#from flask import jsonify
import numpy

app = flask.Flask(__name__)
app.config["DEBUG"] = True

df = pd.read_excel("german_credit.xlsx")
comp = lzhw.CompressedDF(df)

columns = []
for c in range(len(comp.compressed)):
    com = comp.compressed[c].compressed
    if isinstance(com, numpy.ndarray):
        com = list(com.astype(str))
    com = list(map(str, list(com)))
    columns.append(com)
	
seqs = []
for s in range(len(comp.compressed)):
	seqs.append(comp.compressed[c].sequences)
	
comp_dict = {"columns": columns, "Sequences": seqs}

@app.route('/full', methods=['GET'])
def get_full():
	start = time()
	try:
		return df.to_json()
	finally:
		print(time() - start)
	
	
@app.route('/compressed', methods=['GET'])
def get_compressed():
	start = time()
	try:
		return comp_dict
	finally:
		print(time() - start)

app.run()