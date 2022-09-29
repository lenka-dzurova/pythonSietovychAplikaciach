from ast import Num
from fcntl import F_OFD_GETLK
import imp
from re import L


from models.MovieModel import MovieModel

class MovieLibralyService():
    def __init__(self) -> None:
        self.movies:list = list()
        pass

    def addMovie(self, paMovie:MovieModel):
        self.movies.append(paMovie)
        pass

    def removeModel(self, paMovieIndex:Num):
        self.movies.pop(paMovieIndex)
        pass

    def to_string(self):
        print("*************** MOVIE LIBRALY **************************")
        for movie in self.movie:
            print(movie)
            print("")
        print("")
