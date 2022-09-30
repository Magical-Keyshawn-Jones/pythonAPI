from typing import Optional
from xmlrpc.client import boolean
from fastapi import Body, FastAPI, Response, APIRouter
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# module.exports = {
#     getAll,
#     getById,
#     create,
#     update,
#     remove,
# }

# Used for routes
router = APIRouter()
# Used to invoke/actually used router  
# server.include_router(<name of router>)

server = FastAPI()

# Connecting to database
while True:
    try:
        # connect = psycopg2.connect(host, database, user, password)
        connect = psycopg2.connect(host = 'localHost', 
        database = 'PYTHONAPI', user = 'killz', password = '2', 
        cursor_factory = RealDictCursor)

        # Cursor is used to interact the database
        cursor = connect.cursor()
        print('DataBase Connected')
        break
    except Exception as error:
        print('Failed to connect to database')
        print(error)
        time.sleep(2)

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
    cursor.execute(""" SELECT * FROM products """)
    data = cursor.fetchall()
    print(data)
    # return dataArray
    return data

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
# Post is being stored as Payload variable
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
def gettingId(id: int, response: Response):
    # Always convert id to an int
    # print(type(id))

    post = dataFinder(int(id))
    if not post:
        response.status_code = 404

    return post

@server.delete('/somethingTest/{id}')
def deletePost(id: int):
    index = indexFinder(id)
    dataArray.pop(index)
    return {'message': 'done and done'}

def dataFinder(id):
    # x is what is inside the dataArray
    for x in dataArray:
        if x["id"] == id:
            return x

def indexFinder(id):
    # Use enumerated to find the index. "Y" is the index and "X" is the item in the array
    for y, x in enumerate(dataArray):
        if x['id'] == id:
            return y

