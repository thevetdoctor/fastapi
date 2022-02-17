from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

db = []


class User(BaseModel):
    id: Optional[int]
    name: str
    mobile: str
    location: str
    hobbies: List[str]

    class Config:
        schema_extra = {
            'example': {
                'name': 'Oba',
                'mobile': '08069100463',
                'location': 'Ibadan',
                'hobbies': ['reading', 'swimming']
            }
        }


@app.get('/')
def root():
    return {'message': 'Hello Everyone, this is fastAPI !'}


@app.get('/users')
def all_users():
    return {'users': db}


@app.post('/users')
def add_user(user: User):
    db.append(user)
    return {'users': db}


@app.get('/users/{id}')
def get_user(id: int):
    if id > len(db) or id < 1:
        return {
            'error': 'Invalid ID passed'
        }
    for item in db:
        try:
            if db[id]:
                return {
                    'data': [
                        item
                    ]
                }
        except:
            print('Error found')
            return {'error': 'Item with ID {} was not found'.format(id)}
    return {'error': 'No such item with ID {} exist'.format(id)}
