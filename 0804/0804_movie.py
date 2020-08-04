import requests
from bs4 import BeautifulSoup
import csv
import re

movie_data = []

URL='https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup= BeautifulSoup(response.text, 'html.parser')


movie_section = soup.select(
    '#content > div.article > div.obj_section > div.lst_wrap > ul > li')

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    
    data_dict = {}

    title = a_tag.get_text()

    href = a_tag['href']
    href_splitted = href.split('=')
    code = href_splitted[-1]

    data_dict[title] = code

    movie_data.append(data_dict)

print(movie_data)