import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()


# pylint: disable=missing-docstring, C0103

def directors_count(db):
    query = 'SELECT COUNT(*) FROM directors d'
    db.execute(query)
    results = db.fetchone()
    return results[0]

    # return the number of directors contained in the database
def directors_list(db):
    query = 'SELECT dir.name FROM "directors" AS dir ORDER BY dir.name ASC'
    db.execute(query)
    results = db.fetchall()
    sol_list = []
    for i in results:
        sol_list.append(i[0])
    return sol_list
#directors_list(db)
    # return the list of all the directors sorted in alphabetical order

def love_movies(db):
    query = '''SELECT mov.title FROM "movies" AS mov
    WHERE UPPER(mov.title) LIKE "% LOVE %"
    OR UPPER(mov.title) LIKE "LOVE %"
    OR UPPER(mov.title) LIKE "% LOVE"
    OR UPPER(mov.title) LIKE "LOVE"
    OR UPPER(mov.title) LIKE "LOVE,%"
    OR UPPER(mov.title) LIKE '% LOVE''%'
    OR UPPER(mov.title) LIKE "% LOVE."
    ORDER BY mov.title ASC'''
    db.execute(query)
    results = db.fetchall()
    sol_list = []
    for i in results:
        sol_list.append(i[0])
    return sol_list
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order


def directors_named_like_count(db, name):
    query = f'SELECT COUNT(dir.name) FROM "directors" AS dir WHERE UPPER(dir.name) LIKE UPPER("%{name}%")'
    db.execute(query)
    results = db.fetchone()
    return int(results[0])
    # return the number of directors which contain a given word in their name


def movies_longer_than(db, min_length):
    query = f'SELECT mov.title FROM movies AS mov WHERE mov.minutes > {min_length} ORDER BY mov.title ASC'
    db.execute(query)
    results = db.fetchall()
    sol_list = []
    for i in results:
        sol_list.append(i[0])
    print(sol_list)
    return sol_list

    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
#for loop and list
