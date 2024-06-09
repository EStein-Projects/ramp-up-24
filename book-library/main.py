from fastapi import FastAPI
import schemas


app = FastAPI()

books = {
    # Sample group of books:
    # 1: {"Title": "How to", "Author": "Ploni Amoni", "Publication Year": 2723},
    # 2: {"Title": "The Adventures of", "Author": "You-Know-Who", "Publication Year": 5757},
    # 3: {"Title": "Stories of", "Author": "A. Nanny Muss", "Publication Year": 2024}
}

@app.get("/books/")
def get_books():
    return books

@app.get("/books/{id}")
def get_book(id:int):
    return books[id]

@app.post("/books/")
def add_book(book:schemas.Book):
    new_id = len(books.keys())+1
    books[new_id] = {"Title": book.title, "Author": book.author, "Publication Year": book.year}
    return {new_id: books[new_id]}

@app.put("/books/{id}")
def update_book(id:int, book:schemas.Book):
    books[id]["Title"] = book.title
    books[id]["Author"] = book.author
    books[id]["Publication Year"] = book.year

@app.delete("/books/{id}")
def delete_book(id:int):
    del books[id]