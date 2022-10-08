from ast import Num
from models.MovieModel import MovieModel


class MovieLibralyService():
    def __init__(self) -> None:
        self.movies:list(MovieModel) = list()
        pass

    def addMovie(self, paMovie:MovieModel):
        self.movies.append(paMovie)
        pass

    def removeModel(self, paMovieIndex:Num):
        self.movies.pop(paMovieIndex)
        pass

    def to_string(self):
        print("*************** MOVIE LIBRALY **************************")
        for movie in self.movies:
            print(movie.to_string())
            print("")
        print("")
