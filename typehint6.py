from typing import TypedDict, List

class Movie(TypedDict):
    title: str
    year: int
    genres: List[str]

my_movie: Movie = {
    "title": "Inception",
    "year": 2010,
    "genres": ["Sci-Fi", "Thriller"]
}
