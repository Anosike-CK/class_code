import csv
import pymysql

with open('films.csv', encoding='utf-8') as file:

    csv_file = csv.DictReader(file)
    # csv_file = csv.reader(file, fieldnames= ('adult','budget','genres','popularity','production_companies','production_countries','release_date','revenue','runtime','spoken_languages','title','vote_average'))
    i = 0
    for line in csv_file:
        i += 1
        print(line)
        if i == 10:
            break
  
