# JustJoin.IT Scraper

Skrypt pobierający oferty pracy z JustJoin.IT i generujący raporty w Excelu i HTML.

## Instalacja
```bash
pip install -e .
```

## Użycie

Pobierz oferty:
```bash
jjit scrape
```

## Wygeneruj raport:
```bash
jjit report
```

Raporty znajdziesz w folderze `output/` — plik Excel i dashboard HTML.

## Opcjonalnie

Możesz podać własną nazwę pliku:
```bash
jjit scrape plik.json
jjit report plik.json
```

Zapis do bazy danych SQLite:
```bash
jjit report --format sqlite
```

Plik bazy danych znajdziesz w `output/offers.db`.