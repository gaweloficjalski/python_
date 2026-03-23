import json
import os
from pathlib import Path

def export_to_html(results, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    cities_labels = json.dumps(list(results['top_cities'].index))
    categories_labels = json.dumps(list(results['top_categories'].index))
    salary_labels = json.dumps(list(results['avg_salary_per_categories'].index))  # zmiana: per category
    experience_labels = json.dumps(list(results['experience_levels'].index))
    cities_values = json.dumps(list(results['top_cities'].values), default=int)
    categories_values = json.dumps(list(results['top_categories'].values), default=int)
    salary_values = json.dumps(list(results['avg_salary_per_categories'].values), default=int)  # zmiana
    experience_values = json.dumps(list(results['experience_levels'].values), default=int)

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>JustJoin.IT Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; background: #0F172A; color: #E2E8F0; padding: 24px; }}
        h1 {{ color: #0EA5E9; text-align: center; margin-bottom: 24px; font-size: 1.6rem; letter-spacing: -0.3px; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        .card {{ background: #1E293B; border: 1px solid #334155; border-radius: 12px; padding: 20px; }}
        .card h2 {{ font-size: 0.8rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.6px; margin-bottom: 14px; }}
        .chart-wrap {{ position: relative; height: 260px; }}
        .chart-wrap.small {{ height: 200px; width: 200px; margin: 0 auto; }}
    </style>
</head>
<body>
    <h1>Dashboard</h1>
    <div class="grid">
        <div class="card">
            <h2>Top cities</h2>
            <div class="chart-wrap"><canvas id="citiesChart"></canvas></div>
        </div>
        <div class="card">
            <h2>Category</h2>
            <div class="chart-wrap"><canvas id="categoriesChart"></canvas></div>
        </div>
        <div class="card">
            <h2>Average earnings</h2>
            <div class="chart-wrap"><canvas id="salaryChart"></canvas></div>
        </div>
        <div class="card">
            <h2>Experience</h2>
            <div class="chart-wrap small"><canvas id="experienceChart"></canvas></div>
        </div>
    </div>

    <script>
        const gridColor = 'rgba(255,255,255,0.06)';
        const tickColor = '#94A3B8';

        const citiesLabels = {cities_labels};
        const citiesValues = {cities_values};
        const categoriesLabels = {categories_labels};
        const categoriesValues = {categories_values};
        const salaryLabels = {salary_labels};
        const salaryValues = {salary_values};
        const experienceLabels = {experience_labels};
        const experienceValues = {experience_values};

        new Chart(document.getElementById('citiesChart'), {{
            type: 'bar',
            data: {{ labels: citiesLabels, datasets: [{{ label: 'Oferty', data: citiesValues, backgroundColor: '#0EA5E9', borderRadius: 4 }}] }},
            options: {{
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    x: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }},
                    y: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }}
                }}
            }}
        }});

        new Chart(document.getElementById('categoriesChart'), {{
            type: 'bar',
            data: {{ labels: categoriesLabels, datasets: [{{ label: 'Oferty', data: categoriesValues, backgroundColor: '#22C55E', borderRadius: 4 }}] }},
            options: {{
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    x: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }},
                    y: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }}
                }}
            }}
        }});

        new Chart(document.getElementById('salaryChart'), {{
            type: 'bar',
            data: {{ labels: salaryLabels, datasets: [{{ label: 'Średnia PLN', data: salaryValues, backgroundColor: '#0EA5E9', borderRadius: 4 }}] }},
            options: {{
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    x: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }},
                    y: {{ ticks: {{ color: tickColor }}, grid: {{ color: gridColor }} }}
                }}
            }}
        }});

        new Chart(document.getElementById('experienceChart'), {{
            type: 'doughnut',
            data: {{ labels: experienceLabels, datasets: [{{ data: experienceValues, backgroundColor: ['#4A1B2A','#0EA5E9','#22C55E','#F59E0B'], borderColor: '#1E293B', borderWidth: 2 }}] }},
            options: {{
                cutout: '60%',
                plugins: {{ legend: {{ position: 'bottom', labels: {{ color: tickColor, font: {{ size: 11 }} }} }} }}
            }}
        }});
    </script>
</body>
</html>"""

    Path(filepath).write_text(html, encoding='utf-8')