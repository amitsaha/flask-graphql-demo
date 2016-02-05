from schema import schema
from flask_graphql import GraphQL
from flask import Flask, request, jsonify

app = Flask(__name__)
GraphQL(app, schema=schema)

if __name__ == '__main__':
    app.run(debug=True)
