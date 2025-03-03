from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import asyncio
import db

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test api

count = 0

class UserModel(BaseModel):
    name : str

@app.post("/count")
async def count_up():
    global count
    count += 1
    return {"count":count}

@app.get("/count")
async def get_count():
    global count
    return {"count":count}

@app.post("/user")
async def create_user(payload : UserModel):
    db_user = db.create_user(payload.name)
    if db_user:
        return {"name" : db_user.name}
    else:
        return "faild"

@app.get("/users")
async def get_users():
    db_users = db.get_users()
    
    return db_users

# Test api
async def run_fastapi():
    
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(run_fastapi())       
    except (KeyboardInterrupt,SystemExit):
        print('INFO:     SHUTDOWN')