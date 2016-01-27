from app import app
import pytest
import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

#XXX: Todo, we also want to setup our data here ..

@pytest.fixture
def client():
    return app.test_client()

def test_basic_query(client):
    """ Basic query test """
    expected_response = '{"data":{"person":{"name":"Jack"}}}'
    response = client.get('/graphql?query=query something{person(id:1){name}}')
    assert response.data == expected_response

def test_mutation_update(client):
    """ Basic mutation which updates existing data """
    query = json.dumps(
        {'query':
         '''mutation M {
              updatePerson(id: 1,name: "New Name") {
                    person {
                       id name age
                    }
              }
            }
       '''
    })
    response = client.post(
        '/graphql',
        data=query,
        content_type='application/json'
    )
    expected_response = '{"data":{"updatePerson":{"person":{"id":1,"name":"New Name","age":34.0}}}}'
    assert response.data == expected_response

def test_mutation_file_upload(client):
    """ Mutation which uploads a file """
    query = '''mutation M {
              updatePerson(id: 1,avatar: "cat1.jpg") {
                    person {
                       id name age avatar
                    }
              }
            }
       '''
    data = {
        'query': query,
        'file': (open('files/cat1.jpg'), 'cat1.jpg'),
    }
    response = client.post(
        '/graphql', data=data,
        content_type='multipart/form-data',
    )

    expected_response = '{"data":{"updatePerson":{"person":{"id":1,"name":null,"age":34.0,"avatar":"/files/cat1.jpg"}}}}'
    assert response.data == expected_response
