from typing import Optional
from xmlrpc.client import boolean
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

server = FastAPI()

# Schema Validation
class Post(BaseModel):
    title: str
    content: str

    # "=" means defaults to this value if empty
    published: bool = True

    # completely optional
    rating: Optional[int] = None

# Storing Data
# Data only saves if post and get are on the same url
dataArray = [
    {
        'title': 'Dah Baby',
        'content': 'is trash',
        'published': False,
        'rating': 20,
        'id': 1
    }
]

@server.get('/')
async def welcomeMessage():
    return {"message": "Hello World"}

@server.get('/somethingTest')
def getData():
    return dataArray

@server.get('/something')
def randomMessage():
    return {'message': 'Git gud m8'}

@server.post('/something')
def hateMail(payload: dict = Body(...)):
    print(payload)
    # return payload
    # f<-- f"I have a book called {payload['title']}" ONLY works with "" NOT '' or ``
    # f works like `I have a book called ${payload.title}`
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}

@server.post('/somethingTest')
def somethingTest(payload: Post):
    print(payload)

    # dict() prints an object of the payload
    # print(payload.dict())
    bestData = payload.dict()
    bestData['id'] = randrange(0, 999999999)
    dataArray.append(bestData)
    return bestData
    # return {
    #     "Book_title": payload.title,
    #     "summary": f"This book actually {payload.content}"
    # }


@server.get('/somethingTest/{id}')
# Giving this a type will ensure will restrict it to only that type. Automatically converts string to numbers with "int"
# def gettingId(id):
def gettingId(id: int):
    # Always convert id to an int
    # print(type(id))

    post = dataFinder(int(id))
    return post

def dataFinder(id):
    # x is what is inside the dataArray
    for x in dataArray:
        if x["id"] == id:
            return x