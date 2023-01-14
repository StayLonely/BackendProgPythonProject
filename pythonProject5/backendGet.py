import csv
with open('vacancies_with_skills.csv', newline= '') as csvfile:
    reader = csv.DictReader(csvfile)

    with open('backendProgOnly.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['name', 'salary_from','salary_to' ,'salary_currency' , 'area_name', 'published_at']
        writer = csv.writer(csvfile, dialect=csv.unix_dialect)
        writer.writerow((fieldnames))
        for row in reader:
            if('backend-программист' in str(row['name']) or 'Backend-программист' in str(row['name']) \
                    or 'backend' in str(row['name']) or 'бэкэнд' in str(row['name']) \
                    or 'бэкенд' in str(row['name']) or 'бекенд' in str(row['name']) \
                    or 'бекэнд' in str(row['name']) or 'back end' in str(row['name']) \
                    or 'бэк энд' in str(row['name']) or 'бэк енд' in str(row['name']) \
                    or 'django' in str(row['name']) or 'flask' in str(row['name']) \
                    or 'symfony' in str(row['name']) or 'laravel' in str(row['name']) or 'yii' in str(row['name'])):

                writer.writerow([row['name'], row['salary_from'],row['salary_to'], row['salary_currency'], row['area_name'], row['published_at']])