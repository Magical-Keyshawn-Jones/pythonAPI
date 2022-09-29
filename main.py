from fastapi import Body, FastAPI

server = FastAPI()

@server.get('/')
async def welcomeMessage():
    return {"message": "Hello World"}

@server.get('/something')
def randomMessage():
    return {'message': 'Git gud m8'}

@server.post('/something')
def hateMail(payload: dict = Body(...)):
    print(payload)
    return payload