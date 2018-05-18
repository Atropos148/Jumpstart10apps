import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,'
    'imdb_score,keywords,genres'
)


def find_movies(search):
    if not search or not search.strip:
        raise ValueError('Error: Search text is required')

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

    response = requests.get(url)
    response.raise_for_status()

    movie_data = response.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)

    return movies
