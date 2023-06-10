from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from enum import Enum
from typing import Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title = "Test"
)



genre_fake = [
    {"id": 1, "name_genre": "horror", "description": "Scary stories", "author_id": 1, "book_id": 1},
    {"id": 2, "name_genre": "fantasy", "description": "Fantasy stories", "author_id": 2, "book_id": 2},
]

class Genre(BaseModel):
    id: int
    name_genre: str
    description: str
    author_id: int
    book_id: int


authors_fake = [
    {"id": 1, "surname": "Gogol", "name": "Nikolai", "secname": "Vasilievich", "date_of_birth": "", "date_of_death": "", "genre_id": 1, "book_id": 1},
    {"id": 2, "surname": "Puskin", "name": "Alexandr", "secname": "Sergeevich", "date_of_birth": "", "date_of_death": "", "genre_id": 2, "book_id": 2},
]

class Author(BaseModel):
    id: int
    surname: str
    name: str
    secname: str
    date_of_birth: str
    date_of_death: str
    genre_id: int
    book_id: int



fake_books = [
    {"id": 1, "name": "Viy", "numer": 15, "rating": 5, "authors_id": 1, "genre_id": 1},
    {"id": 2, "name": "Evgeniy Onegin", "numer": 180, "rating": 9, "authors_id": 2, "genre_id": 2},
]


class Book(BaseModel):
    id: int
    name: str
    numer: int
    rating: int = Field(ge=0, le=10)
    authors_id: int
    genre_id: int

@app.get("/genres/{genre_id}", response_model=list[Genre])
def get_genre(genre_id: int):
    return [genre for genre in genre_fake if genre.get("id") == genre_id]

@app.post("/genres")
def add_genres(genre: list[Genre]):
    genre_fake.extend(genre)
    return {"status": 200, "data": genre_fake}


# для поиска жанра в списке genre_fakes
def find_genre(id):
   for genre in genre_fake: 
        if genre.get("id") == id:
           return genre
   return None


@app.delete("/genres/{genre_id}")
def delete_genre(genre_id: int):
    genre = find_genre(genre_id)
    genre_fake.remove(genre)
    return genre_fake


@app.get("/genres")
def get_genre_(limit: int = 4, offset: int = 0):
    return genre_fake[offset:][:limit]

@app.put("/genres/{genre_id}", response_model=Genre)
async def update_item(genre_id: int, item: Genre):
    update_item_encoded = jsonable_encoder(item)
    genre_fake[genre_id] = update_item_encoded
    return update_item_encoded


@app.get("/authors/{author_genre_id}", response_model=Author)
def get_author_genre_id(author_genre_id: int):
    for author in authors_fake:
        if author.get("genre_id") == author_genre_id:
            return author



@app.get("/books/{book_genre_id}", response_model=Book)
def get_book_genre_id(book_genre_id: int):
    for book in fake_books:
        if book.get("genre_id") == book_genre_id:
            return book



@app.post("/books")
def add_book(book: list[Book]):
    fake_books.extend(book)
    return {"status": 200, "data": fake_books}


def find_book(id):
   for book in fake_books: 
        if book.get("id") == id:
           return book
   return None


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = find_book(book_id)
    fake_books.remove(book)
    return fake_books


@app.get("/books/{book_id}", response_model=list[Book])
def get_book(book_id: int):
    for book in fake_books:
        if book.get("id") == book_id:
            return book
        

@app.get("/books")
def get_books_(limit: int = 10, offset: int = 0):
    return fake_books[offset:][:limit]



@app.put("/books/{book_id}", response_model=Book)
async def update_item_book(book_id: int, item: Book):
    update_item_encoded = jsonable_encoder(item)
    fake_books[book_id] = update_item_encoded
    return update_item_encoded



@app.post("/authors")
def add_author(author: list[Author]):
    authors_fake.extend(author)
    return {"status": 200, "data": authors_fake}



def find_author(id):
   for author in authors_fake: 
        if author.get("id") == id:
           return author
   return None


@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    author = find_author(author_id)
    authors_fake.remove(author)
    return authors_fake


@app.get("/authors")
def get_authors_(limit: int = 10, offset: int = 0):
    return authors_fake[offset:][:limit]



@app.get("/authors/{author_id}", response_model=list[Author])
def get_author(author_id: int):
    return [author for author in authors_fake if author.get("id") == author_id]


@app.put("/authors/{author_id}", response_model=Author)
async def update_item_author(author_id: int, item: Author):
    update_item_encoded = jsonable_encoder(item)
    authors_fake[author_id] = update_item_encoded
    return update_item_encoded