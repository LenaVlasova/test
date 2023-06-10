from sqlalchemy import MetaData, Table, Column, JSON, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime


metadata = MetaData()



books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("numer", Integer),
    Column("rating", Integer),
    Column("authors_id", Integer, ForeignKey("authors.id")),
    Column("genre_id", Integer, ForeignKey("genre.id"))
)


authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("surname", String, nullable=False),
    Column("name", String, nullable=False),
    Column("secname", String, nullable=False),
    Column("date_of_birth", String, nullable=False),
    Column("date_of_death", String, nullable=False),
    Column("books_id", Integer, ForeignKey("books.id")),
    Column("genre_id", Integer, ForeignKey("genre.id"))
)

genre = Table(
    "genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name_genre", String, nullable=False),
    Column("description", String, nullable=False),
    Column("authors_id", Integer, ForeignKey("authors.id")),
    Column("books_id", Integer, ForeignKey("books.id"))
)
