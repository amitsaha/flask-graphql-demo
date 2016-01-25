## Introduction

This is a simple Flask application demonstrating the usage of [graphql-flask](https://pypi.python.org/pypi/graphql-flask).

##Usage

Star the server:

```
$ pip install -r requirements.txt
$ python app.py
```

The following queries use the `httpie` command line client.

Basic Query:


```
$ http "http://127.0.0.1:5000/?query=query something{person(id:1){name}}"
HTTP/1.0 200 OK
Content-Length: 40
Content-Type: application/json
Date: Wed, 25 Nov 2015 03:29:59 GMT
Server: Werkzeug/0.11.2 Python/2.7.10

{
    "person": {
            "name": "Jack"
    }
}
```

Output:

```
{
person: {
    name: "Jack"
    }
}
```

Mutation to update a person's data:

```

$ http "http://127.0.0.1:5000/?query=mutation%20M%20{%20updateJack:updatePerson(id:%201,%20name:%20%22Hello1%22)%20{%20person%20{%20id%20name%20age%20}%20}%20}"

HTTP/1.0 200 OK
Content-Length: 106
Content-Type: application/json
Date: Thu, 26 Nov 2015 05:59:30 GMT
Server: Werkzeug/0.11.2 Python/2.7.10

{
    "updateJack": {
        "person": {
            "age": 34.0, 
            "id": 1, 
            "name": "Hello1"
        }
    }
}


```

Mutation + file uploads:

```
$ http --form "http://127.0.0.1:5000/?query=mutation%20M%20{%20updateJack:updatePerson(id:%201,%20name:%20%22Hello1%22)%20{%20person%20{%20id%20name%20age%20avatar}%20}%20}" filedata@~/cat1.jpg
HTTP/1.0 200 OK
Content-Length: 142
Content-Type: application/json
Date: Thu, 26 Nov 2015 06:11:28 GMT
Server: Werkzeug/0.11.2 Python/2.7.10

{
    "updateJack": {
        "person": {
            "age": 34.0, 
            "avatar": "/files/cat1.jpg", 
            "id": 1, 
            "name": "Hello1"
        }
    }
}
```

