import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'director title year score')

def get_movies_by_director(data):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    with open(data, newline='',encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        keep = ['director_name', 'movie_title', 'title_year', 'imdb_rating']
        for row in reader if keep in headers:
            print(row)

    return



def get_average_scores(movies):
    '''Filter directors with < MIN_MOVIES and calculate averge score''' 
    return directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    pass


def print_results(movies):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    pass


def main():
    
    get_movies_by_director(MOVIE_DATA)
    

if __name__ == '__main__':
    main()
