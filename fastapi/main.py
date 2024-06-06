from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{name}")
async def helloWorld(name: str):
    return f"Hello, {name}"