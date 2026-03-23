# Pobieranie danych z API

import requests
import time
import json

BASE_URL = "https://justjoin.it/api/candidate-api/offers"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def get_offers(from_value):
    params = {
        "from": from_value,
        "itemsCount": 100
    }
    r = requests.get(BASE_URL, headers=HEADERS, params=params)
    data = r.json()
    # 200 - ok, 429 - za dużo zapytań, 500 - błąd serwera
    if r.status_code != 200:
        print(f'Status code {r.status_code}')
        return None
    return data

def get_all_offers(max_offers=99999):
    all_offers = []
    page = 0
    while True:
        offers = get_offers(page)
        if not offers:
            break
        all_offers.extend(offers['data'])
        ilosc_ofert = len(all_offers)
        if ilosc_ofert >= max_offers:
            break
        print(f'Zebrano: {ilosc_ofert} ofert | Page: {page}')
        page += 100
    return all_offers

if __name__=="__main__":
    full_data = get_all_offers()
    with open('data/offers.json', 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print("Zapisano")
