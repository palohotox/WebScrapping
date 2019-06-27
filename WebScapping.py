
from bs4 import BeautifulSoup
import requests
import random
import csv

def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()


def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def imd_movie_picker():

 #newline='' to remove extract blank column
 with open('TopMovie.csv', mode='w' ,newline='') as myfile:

    my_write = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #print("--------------------------------------------")
    ctr = 0
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)

        # Replace print to write to file no,title,year,url,summary

        #combine element in CSV as list
        my_write.writerow([movie_title,movie_year,movie_summary])
        # This will write to CSV but having empty line between rows

            #myfile.write("%s\n" % movie_title)
            #myfile.writelines("%s\n" % movie_year)

        #print(movie_title, movie_year)
        #print(movie_summary)
        #print("--------------------------------------------")

        print(ctr, " rows generated")
        ctr = ctr + 1
        if (ctr == 100):
            break;


if __name__ == '__main__':
    imd_movie_picker()
