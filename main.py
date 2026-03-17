# Main - odpala wszystko

from src.scraper import get_all_offers
from src.processor import load_offers, extract_salary, extract_category, clean_cities, analyze
from src.exporter import export_to_excel
from src.dashboard import export_to_html

import json
import pandas as pd

def main():
    # pobieranie
    full_data = get_all_offers()
    with open('data/offers.json', 'w', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=2)
    print(f"Pobrano {len(full_data)} ofert")

    # przetwarzanie
    df = load_offers('data/offers.json')
    df[['salary_from', 'salary_to']] = df['employmentTypes'].apply(extract_salary).tolist()
    df['category_name'] = df['category'].apply(extract_category).tolist()
    df['salary_avg'] = ((df['salary_from'] + df['salary_to'])) / 2
    df = clean_cities(df)
    analiza = analyze(df)

    # eksport
    export_to_excel(df, analiza, 'output/report.xlsx')
    export_to_html(analiza, 'output/dashboard.html')

if __name__ == "__main__":
    main()