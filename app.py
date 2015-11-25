from schema import schema
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    query = request.args.get('query')
    # We have files
    # if request.method == 'POST':
    #     file_data = request.files['filedata']

    result = schema.execute(query, root=object())
    if result.data:
        return jsonify(result.data)
    else:
        return jsonify(
            {
                'status':500,
                'message': 'Bad Query', # Send better error back to the client
            }
    )

if __name__ == '__main__':
    app.run(debug=True)
