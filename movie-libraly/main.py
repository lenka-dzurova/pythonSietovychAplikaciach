from services.MovieLibralyService import MovieLibralyService
from models.MovieModel import MovieModel
she_hulk = MovieModel('She-Hulk: Neuveriteľná právnička ', 
                    'V seriáli She-Hulk: Neuveriteľná právnička od štúdia Marvel musí Jennifer Waltersová - právnička zaoberajúca sa právnymi prípadmi spojenými so superľuďmi - žiť komplikovaným životom single ženy po tridsiatke, ktorá je zhodou náhod tiež zelená, dvojmetrová a supersilná obryňa',
                    2022,
                    ["Akčný" , "Dobrodružný" , "Sci-Fi" , "Komédia" , "Dráma"],
                    50)


movie_libraly = MovieLibralyService()
movie_libraly.addMovie(she_hulk)
movie_libraly.addMovie(she_hulk)

movie_libraly.to_string()
movie_libraly.removeModel(0)
movie_libraly.to_string()

#print(she_hulk.to_string())
