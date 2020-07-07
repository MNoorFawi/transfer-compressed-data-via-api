import flask
import lzhw
from time import time
import pandas as pd
from flask import jsonify, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

df = pd.read_csv("1500000 Sales Records.csv")
comp = lzhw.CompressedDF(df)
for i in range(len(df.columns)):
	comp.compressed[i].compressed = [bin(i)[2:] for i in comp.compressed[i].compressed]


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
	try:
		start = time()
		return jsonify({"sequences": comp.compressed[col].sequences, "compressed": comp.compressed[col].compressed})
	finally:
		print(time() - start)

if __name__ == "__main__":
	app.run()
