from fastapi import FastAPI
from API.VideoGames import videoGamesRoute

# Defining our Server
server = FastAPI()

@server.get('/')
def welcomeUser():
    return {"message": "Welcome to my API!"}

# Using our Video Games router
server.include_router(videoGamesRoute.router)