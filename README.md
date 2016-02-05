## Introduction

This is a simple Flask application demonstrating the usage of
[Flask-graphql](https://pypi.python.org/pypi/Flask-graphql). In
addition to querying the data, it demonstrates updating the existing
data as well as file uploads (mutation).


[![Build Status](https://travis-ci.org/amitsaha/flask-graphql-demo.svg?branch=master)](https://travis-ci.org/amitsaha/flask-graphql-demo)


## Usage

Star the server:

```
$ pip install -r requirements.txt
$ python app.py
```

You should now be able to send queries to the `graphql/` endpoint.

### Examples

Please see `test_app.py` for basic examples.

## GraphiQL interface

Thanks to `graphql-flask`, by default the web application also exposes
a graphiql endpoint. Open `http://127.0.0.1:5000/graphiql` in your
browser to play with it.

## Development

Run tests using ``py.test``.
