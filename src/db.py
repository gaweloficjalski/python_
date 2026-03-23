import sqlite3

def save_to_sqlite(df, filepath):
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS offers (
            guid TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            city TEXT,
            workplace_type TEXT,
            working_time TEXT,
            experience_level TEXT,
            category TEXT,
            salary_from REAL,
            salary_to REAL,
            salary_avg TEXT
        )
    ''')
    
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO offers 
            (guid, title, company, city, workplace_type, working_time, experience_level, category, salary_from, salary_to, salary_avg)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row.get('guid'),
            row.get('title'),
            row.get('companyName'),
            row.get('city'),
            row.get('workplaceType'),
            row.get('workingTime'),
            row.get('experienceLevel'),
            row.get('category_name'),
            row.get('salary_from'),
            row.get('salary_to'),
            row.get('salary_avg'),
    ))
    conn.commit()
    conn.close()
    print(f"Saved {len(df)} offers to {filepath}")