import re
import requests
from bs4 import BeautifulSoup

from apis import movie_search_func
from movie.models import ReservationMovie, Movie


def reservation_search():
    response = requests.get('http://movie.daum.net/premovie/scheduled?opt=reservation')
    bs = BeautifulSoup(response.text, "html.parser")
    movie_title_list = bs.select("ul.list_boxthumb li div.desc_boxthumb strong")
    movie_key_elements = bs.select("ul.list_boxthumb li a.link_boxthumb")
    reservation_elements = bs.select("ul.list_boxthumb div.desc_boxthumb dl.list_state")

    for i in range(len(movie_title_list)):
        # 파싱한 영화 제목으로 영화 DB에 저장
        movie_title = movie_title_list[i].text
        print(movie_title)
        try:
            movie_search_func(movie_title)
        except:
            pass

        # 다음 영화ID 파싱 후 DB에서 Foreignkey 추출
        movie_key_element = movie_key_elements[i]
        movie_key_list = re.findall(r'\d+', movie_key_element['href'])
        movie_key = movie_key_list[0]
        print(movie_key)
        movie = Movie.objects.get(daum_id=movie_key)
        print(movie)

        # 개봉일 파싱
        release_date_element = reservation_elements[i].select('dd')[0].text
        release_date_first = re.findall(r'\b[0-9]{4}[./:][0-9]{1,2}[./:][0-9]{1,2}\b', release_date_element)
        if len(release_date_first) == 0:
            release_date_first = re.findall(r'\b[0-9]{4}[./:][0-9]{1,2}\b', release_date_element)
        release_date = release_date_first[0].replace('.', '-')

        # ReservationMovie instance 생성
        try:
            if len(release_date) == 10:
                ReservationMovie.objects.get_or_create(
                    movie=movie,
                    release_date=release_date,
                )
        except:
            pass
