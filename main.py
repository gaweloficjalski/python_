import argparse
import json
import os
from src.scraper import get_all_offers
from src.processor import load_offers, extract_salary, extract_category, clean_cities, analyze
from src.exporter import export_to_excel
from src.dashboard import export_to_html


def main():
    parser = argparse.ArgumentParser(description='JustJoin.IT Scraper')
    subparsers = parser.add_subparsers(dest='command')

    # scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Fetch offers')
    scrape_parser.add_argument('output', nargs='?' ,default='data/offers.json', help='Output file path')

    # report command
    report_parser = subparsers.add_parser('report', help='Generate report')
    report_parser.add_argument('input', nargs='?' ,default='data/offers.json', help='Input file path')

    args = parser.parse_args()

    if args.command == 'scrape':
        full_data = get_all_offers()
        folder = os.path.dirname(args.output)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(full_data, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(full_data)} offers to {args.output}")

    elif args.command == 'report':
        df = load_offers(args.input)
        df[['salary_from', 'salary_to']] = df['employmentTypes'].apply(extract_salary).tolist()
        df['category_name'] = df['category'].apply(extract_category).tolist()
        df['salary_avg'] = ((df['salary_from'] + df['salary_to'])) / 2
        df = clean_cities(df)
        analiza = analyze(df)
        export_to_excel(df, analiza, 'output/report.xlsx')
        export_to_html(analiza, 'output/dashboard.html')
        print("Reports saved to output/")


if __name__ == "__main__":
    main()