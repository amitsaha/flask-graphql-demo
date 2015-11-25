##Usage

python app.py

##Examples

Query:

```
http "http://127.0.0.1:5000/?query=query something{person(id:1){name}}"
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
$ http "http://127.0.0.1:5000/?query=mutation M{updateJack:updatePerson(id:1,name:"Jill"){person{id,name,age}}}
HTTP/1.0 200 OK
Content-Length: 104
Content-Type: application/json
Date: Wed, 25 Nov 2015 03:27:37 GMT
Server: Werkzeug/0.11.2 Python/2.7.10

{
    "updateJack": {
        "person": {
            "age": 34.0, 
            "id": 1, 
            "name": "Jill"
        }
    }
}

```

Mutation + file uploads: