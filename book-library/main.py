from fastapi import FastAPI

app = FastAPI()

books = {
    1: {"Title": "How to", "Author": "Ploni Amoni", "Year": 2723},
    2: {"Title": "The Adventures of", "Author": "You-Know-Who", "Year": 5757},
    3: {"Title": "Stories of", "Author": "A. Nanny Muss", "Year": 2024}
}

@app.get("/books/")
def get_items():
    return books

@app.get("/books/{id}")
def get_item(id:int):
    return books[id]

@app.post("/books/")
def add_item(title:str, author:str, publication_date:int):
    books[len(books.keys())+1] = {"Title": title, "Author": author, "Year": publication_date}