import csv
from collections import defaultdict, namedtuple, Counter
from statistics import mean

MOVIE_DATA = 'days/04-06 collections/movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, newline='',encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #can also use try: ... and except ValueError: continue to ignore rows with bad data
            if int(row['title_year'].replace('','0')) >= MIN_MOVIES:
                directors[row['director_name']].append(
                    Movie(row['movie_title'], row['title_year'], row['imdb_score'])
                    )           
    return directors



def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score''' 
    # dictionary with tuples as keys, and lists as values, confusing AF
    directors = {(director, _calc_mean(movies)) : movies for director, movies in directors.items() if len(movies) > MIN_MOVIES}
    return directors

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(mean([float(movie.score.replace('','0')) for movie in movies]),2)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    counter = 1
    for (director, avg), movie in sorted(directors.items(), key = lambda x: x[0][1], reverse=True):
        fmt_director_entry = f'{counter}. {director:<52} {avg}'
        print(fmt_director_entry)
        for item in movie:
            fmt_movie_entry = f'{item.year}] {item.title:<50} {item.score}'
            print(fmt_movie_entry)
        sep_line = '-' * 60     
        print(sep_line)  
        counter += 1
        if counter == 21:
            break
    
    #can also use Counter to get top 20 directors
    #cnt = Counter()
    #for director, movies in directors.items():
        #cnt[director] += len(movies)
    #cnt.most_common(20)
    return 


def main():
    print_results(get_average_scores(get_movies_by_director(MOVIE_DATA)))
    

if __name__ == '__main__':
    main()
