
from ast import Num
from pydoc import describe
from turtle import title

from models.MovieModel import MovieModel
from constants.MovieActionEnum import MenuActionEnum
class MenuView:
    def __init__(self) -> None:
        pass

    def menu(self):
        print("Welcom to Movie Libraly")
        print(f"Add Movie ({MenuActionEnum.ADD_MOVIE})")
        print(f"Remove Movie ({MenuActionEnum.REMOVE_MOVIE})")
        print(f"Show libraly ({MenuActionEnum.SHOW_LIBRALY})")
        print("Quit (q)")
        user_input = input("Select an option from the menu: ")
        return user_input

        
    def add_movie(self):
        title:str = input("ENter movie title")
        description:str = input("Enter movie description")
        year:Num = input("Enter year")
        genre:str = input("Enter movie genre")
        rating:Num = input("Enter ratin in %: ")
        return MovieModel(title,description,year,genre,rating)

    def quit_option(self):
        print("Bye")
        exit(0)
