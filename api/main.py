from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio

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

@app.post("/count")
async def count_up():
    global count
    count += 1
    return {"count":count}

@app.get("/count")
async def get_count():
    global count
    return {"count":count}

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