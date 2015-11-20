from schema import schema
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get('query')
    result = schema.execute(query)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)
