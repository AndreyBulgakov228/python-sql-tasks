import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def add_movies(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO movies (title, release_year, duration) 
            VALUES 
                ('Godfather', 1972, 175),
                ('The Green Mile', 1999, 189)
        """)
    connection.commit()


def get_all_movies(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM movies ORDER BY id")
        return cursor.fetchall()
# END
