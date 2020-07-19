import requests
from bs4 import BeautifulSoup as BS

avto_r = requests.get('https://promokodi.ru/promo-category/avtotovary/')
avto_html = BS(avto_r.content, 'html.parser')

clothes_r = requests.get('https://promokodi.ru/promo-category/odezhda/')
clothes_html = BS(clothes_r.content, 'html.parser')

games_r = requests.get('https://promokodi.ru/promo-category/igry/')
games_html = BS(games_r.content, 'html.parser')

shoes_r = requests.get('https://promokodi.ru/promo-category/obuv/')
shoes_html = BS(shoes_r.content, 'html.parser')

sport_r = requests.get('https://promokodi.ru/promo-category/sport-i-otdyx/')
sport_html = BS(sport_r.content, 'html.parser')

food_r = requests.get('https://promokodi.ru/promo-category/eda/')
food_html = BS(food_r.content, 'html.parser')

computer_r = requests.get('https://promokodi.ru/promo-category/kompyutery-i-elektronika/')
computer_html = BS(computer_r.content, 'html.parser')

tour_r = requests.get('https://promokodi.ru/promo-category/tury-i-puteshestviya/')
tour_html = BS(tour_r.content, 'html.parser')

cool_r = requests.get('https://promokodi.ru/top/')
cool_html = BS(cool_r.content, 'html.parser')

def cool_sales():
    cool = {}
    for el in cool_html.select('.offer-box'):
        title = el.select('.show2line')
        ref = el.find('img').get('data-src')
        cool[title[0]] = ref
    return cool

def auto_sales():
    avto = {}
    for el in avto_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            avto[title[0]] = ref
    return avto


def auto_promo():
    avto = {}
    for el in avto_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            avto[title[0]] = ref
    return avto


def clothes_sales():
    clothes = {}
    for el in clothes_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            clothes[title[0]] = ref
    return clothes


def clothes_promo():
    clothes = {}
    for el in clothes_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            clothes[title[0]] = ref
    return clothes


def games_sales():
    games = {}
    for el in games_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            games[title[0]] = ref
    return games


def games_promo():
    games = {}
    for el in games_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            id = el.select('.offer')
            url = 'https://promokodi.ru/promo-category/avtotovary/#oid' + id[0].get('data-offer-id') + '/'
            promo_check = requests.get(url)
            gamespromo_html = BS(promo_check.content, 'html.parser')
            promo = gamespromo_html.findAll('input')
            title = el.select('.show2line')
            # key = title[0] + promo[0]
            ref = el.find('img').get('data-src')
            games[title[0]] = ref
    return games


def shoes_sales():
    shoes = {}
    for el in shoes_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            shoes[title[0]] = ref
    return shoes


def shoes_promo():
    shoes = {}
    for el in shoes_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            shoes[title[0]] = ref
    return shoes


def sport_sales():
    sport = {}
    for el in sport_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            sport[title[0]] = ref
    return sport


def sport_promo():
    sport = {}
    for el in sport_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            sport[title[0]] = ref
    return sport


def food_sales():
    food = {}
    for el in food_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            food[title[0]] = ref
    return food


def food_promo():
    food = {}
    for el in food_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            food[title[0]] = ref
    return food


def computer_sales():
    computer = {}
    for el in computer_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            computer[title[0]] = ref
    return computer


def computer_promo():
    computer = {}
    for el in computer_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            computer[title[0]] = ref
    return computer


def tour_sales():
    tour = {}
    for el in tour_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text == "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            tour[title[0]] = ref
    return tour


def tour_promo():
    tour = {}
    for el in tour_html.select('.offer-box'):
        label = el.select('.btn-label')
        if label[0].text != "Открыть предложение":
            title = el.select('.show2line')
            ref = el.find('img').get('data-src')
            tour[title[0]] = ref
    return tour
