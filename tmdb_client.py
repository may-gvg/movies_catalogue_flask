
import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTRlN2Q4MzFkNWI5MTlhYjhkODA2MWY5YjcyOTllNiIsInN1YiI6IjYwYzg1NjU2NjZhZTRkMDA1OWM0Y2YyYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dp1D-mYfe1nXvt0-bCw2fupl81BXy-LcyEKh3t5EZMg"


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTRlN2Q4MzFkNWI5MTlhYjhkODA2MWY5YjcyOTllNiIsInN1YiI6IjYwYzg1NjU2NjZhZTRkMDA1OWM0Y2YyYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dp1D-mYfe1nXvt0-bCw2fupl81BXy-LcyEKh3t5EZMg"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTRlN2Q4MzFkNWI5MTlhYjhkODA2MWY5YjcyOTllNiIsInN1YiI6IjYwYzg1NjU2NjZhZTRkMDA1OWM0Y2YyYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dp1D-mYfe1nXvt0-bCw2fupl81BXy-LcyEKh3t5EZMg"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"

    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']


def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']
