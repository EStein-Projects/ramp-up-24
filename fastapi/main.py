from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloWorld(name=input("Enter your name: ")):
    return f"Hello, {name}"