from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests

PRIVATE_KEY = "43772311-6aa0-4391-ad96-c1699750b817"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Private-Key": PRIVATE_KEY}
    )
    return response.json()

