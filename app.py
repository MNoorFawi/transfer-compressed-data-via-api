import flask
import lzhw
from time import time
import pandas as pd
from flask import jsonify, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

df = pd.read_csv("1500000 Sales Records.csv")


@app.route('/full', methods=['GET'])
def get_full():
	col = int(request.args["col"])
	start = time()
	try:
		return df.iloc[:, col].to_json()
	finally:
		print(time() - start)

@app.route('/compressed', methods=['GET'])
def get_compressed():
	col = int(request.args["col"])
	comp = lzhw.CompressedDF(df, selected_cols = [col])
	comp.compressed[0].compressed = [bin(i)[2:] for i in comp.compressed[0].compressed]
	try:
		start = time()
		return jsonify({"sequences": comp.compressed[0].sequences, "compressed": comp.compressed[0].compressed})
	finally:
		print(time() - start)

if __name__ == "__main__":
	app.run()
