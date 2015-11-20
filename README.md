##Usage

python app.py

##Examples

Query:

```
http://127.0.0.1:5000/?query=query%20something{person(id:1){name%20}}
```

Output:

```
{
person: {
    name: "Jack"
    }
}
```
