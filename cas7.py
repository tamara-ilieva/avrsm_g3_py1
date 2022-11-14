# EXERCISE 3
# - Da se presmeta prosek na klasot -> float
# - Da se presmeta prosek za sekoj predmet -> {"mathematics": float, "physics": float ...}
# - Da se sortiraat studentite po azbuchen red (listata students)
# - Ispushten e vnesot na poslednata ocenka (po predmetot Programiranje) kaj del od studentite,
#   no znaeme deka prosekot po ovoj predmet e 4.8. Koristejkji ja ovaa informacija treba da se
#   otkrijat ocenkite i za drugite studenti
# - Da se ispechati koi predmeti imaat povisok prosek od lani -> ["mathematics", "physics"]
# - Da se ispechati razlikata megju prosekot od ovaa godina i od lani za sekoj predmet vo format -> mathematics -> float
# - Da se kreira rechnik za sekoj predmet so slednive informacii: -> {"name": "mathematics", "grades": [], "average": float}
# - Ima greshka pri vnesuvanje na ocenkite kaj nekoi studenti, vneseni se so bukvi namesto so brojki.
#   Da se kreira funkcija kojashto kje izvrshi zamena na bukvite so brojki; a - 5, b - 4, c - 3, d - 2, f - 1

#
# students = [
#     {"name": "Marija", "grades": ['c', 4, 5, 'd'], "avg": 3.5},
#     {"name": "Ilija", "grades": [3, 4, 4, 'b'], "avg": 3},
#     {"name": "Antonio", "grades": [5, 5, 5, 'a']},
#     {"name": "Marko", "grades": [3, 4, 5, 2, 5], "avg": 3.8},
#     {"name": "Martina", "grades": [4, 4, 5, 5, 4]},
# ]
#
# subjects = ["mathematics", "physics", "biology", "geography", "programming"]

last_years_statistics = {
    "mathematics": 4.5,
    "physics": 3.2,
    "biology": 3.9,
    "geography": 4.6,
    "programming": 4.0
}

def formuli(r):
    d = 2*r
    l= 2*r*3.14
    p = r*r*3.14
    return d, l, p
res = formuli(int(input()))
print(res)
