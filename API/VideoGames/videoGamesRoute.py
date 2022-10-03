from asyncio.windows_events import NULL
from turtle import title
from typing import Optional
from unicodedata import name
from unittest import result
from xmlrpc.client import boolean
from fastapi import APIRouter
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pydantic import BaseModel

# Creating datbase variables
host = 'localHost'
database = 'Video Games'
user = 'killz'
password = '2'
cursorFactory = RealDictCursor

# Connecting to Database
while True:
    try: 
        connect = psycopg2.connect(
            host = host, 
            database = database, 
            user = user,
            password = password,
            cursor_factory = cursorFactory
        )

        # Cursor is used to interact the database
        cursor = connect.cursor()
        print('Database Connected')
        break
    except Exception as error: 
        print('Failed to connect to database')
        print(error)
        time.sleep(2)

# Schema Validation
class Message(BaseModel):
    title: str
    rating: Optional[int] = 1
    preOrdered: bool = False
    comment: Optional[str]
    excitement: Optional[str]
    platform: str

class videoGameModel(BaseModel):
    title: str

# Defining our Router
router = APIRouter()

@router.get('/games')
def getAll():
    cursor.execute(""" SELECT * FROM "Video_Games" """)
    results = cursor.fetchall()
    return results

@router.get('/games/titles')
def getAllTitles():
    cursor.execute(""" SELECT "Title" FROM "Video_Games"  """)
    results = cursor.fetchall()
    noDuplicates = []

    for title in results:
        duplicates = []
        if title not in noDuplicates:
            noDuplicates.append(title)
        else:
            duplicates.append(title)
    
    return noDuplicates

@router.post('/games/titles/videoGame')
def getGameByTitle(videoGame: videoGameModel):
    cursor.execute(f""" SELECT * FROM "Video_Games" WHERE "Title" = '{videoGame.title}' """)
    results = cursor.fetchall()
    return results

@router.get('/games/{id}')
def getId(id: int):
    cursor.execute(f""" SELECT * FROM "Video_Games" WHERE "Id" = '{id}' """)
    results = cursor.fetchone()
    print(results)
    if results == None:
        return {"Message": f'Data with that Id does not exist'}
    return results

# Use connect.commit() to commit to changes
@router.post('/games')
def create(payload: Message):
    cursor.execute(""" INSERT INTO "Video_Games" ("Title", "Rating", "PreOrdered", "Comment", "Excitement", "Platform")
    VALUES (%s, %s ,%s, %s, %s, %s) RETURNING * """, 
    (payload.title, payload.rating, payload.preOrdered, payload.comment, payload.excitement, payload.platform))
    results = cursor.fetchone()
    connect.commit()
    return results


@router.delete('/games/{id}')
def delete(id: int):
    cursor.execute(f""" DELETE FROM "Video_Games" WHERE "Id" = '{id}' """)
    connect.commit()
    return {'Message': f'Deleted data with the Id of {id}'}

@router.put('/games/{id}')
def change(id: int, payload: Message):

    cursor.execute(
        f""" UPDATE "Video_Games" SET  "Title" = '{payload.title}', "Rating" = '{payload.rating}', 
        "PreOrdered" = '{payload.preOrdered}', "Comment" = '{payload.comment}', "Excitement" = '{payload.excitement}', 
        "Platform" = '{payload.platform}' WHERE "Id" = {id} """
    )
    connect.commit()

    return getId(id) 
