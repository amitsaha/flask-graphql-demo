from schema import schema
from graphql_flask import GraphQL
from flask import Flask, request, jsonify

app = Flask(__name__)
GraphQL(app, schema=schema)

if __name__ == '__main__':
    app.run(debug=True)
