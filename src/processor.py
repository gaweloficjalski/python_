#Przetwarzanie danych (pandas)

from src.exporter import export_to_excel
from src.dashboard import export_to_html
import pandas as pd
import json

# Załadowanie ofert
def load_offers(filepath):
    with open(filepath, 'r',encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    #print(df.columns.tolist())
    return (df)


# Wyciąganie salary
def extract_salary(employment_types):
    if not employment_types:
        return (None, None)
    for i in employment_types:
        if (i['currency']=='PLN' and i['unit']=='Month'):
            return (i['from'], i['to'])
    return (None, None)


# Wyciąganie kategorii
def extract_category(category):
    if not category:
        return (None)
    return (category['key'])

# Wyciąganie najpopularniejszych skili
def extract_skills(df):
    skills = []
    for skill in df['requiredSkills']:
        for name in skill:
            if 'name' in name:
                skills.append(name['name'])
    result = pd.Series(skills).value_counts().head(20)
    return result


# Analiza miasta-doswiadczenie-kategorie
def analyze(df):
    results = {}
    results['top_cities'] = df['city'].value_counts().head(10)
    results['experience_levels'] = df['experienceLevel'].value_counts()
    results['top_categories'] = df['category_name'].value_counts().head(10)
    results['avg_salary'] = df.groupby('city')['salary_avg'].mean().sort_values(ascending=False).head(10).round(0).astype(int)
    results['avg_salary_per_experience'] = df.groupby('experienceLevel')['salary_avg'].mean().sort_values(ascending=False).head(10).round(0).astype(int)
    results['avg_salary_per_categories'] = df.groupby('category_name')['salary_avg'].mean().sort_values(ascending=False).head(10).round(0).astype(int)
    results['top_skills'] = extract_skills(df)
    #print(results)
    return results

def clean_cities(df):
    CITY_MAP = {
    'Warsaw': 'Warszawa',
    'warsaw': 'Warszawa',
    'WarszaAWA': 'Warszawa',
    'Warszawa (Mazowieckie)': 'Warszawa',
    'Cracow': 'Kraków',
    'Gdansk': 'Gdańsk',
    'Gdańsk (Pomorskie)': 'Gdańsk',
    'Poland remote': 'Poland (Remote)',
    'polska': 'Poland (Remote)',
    }
    POLISH_CITIES = ['Warszawa', 'Kraków', 'Wrocław', 'Gdańsk', 
                 'Poznań', 'Katowice', 'Łódź', 'Rzeszów',
                 'Lublin', 'Szczecin', 'Bydgoszcz', 'Gdynia',
                 'Białystok', 'Toruń', 'Opole', 'Gliwice',
                 'Suwałki', 'Poland (Remote)']
    df['city'] = df['city'].replace(CITY_MAP)
    df = df[df['city'].isin(POLISH_CITIES)]
    return df