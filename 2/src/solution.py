import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def make_cars_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id SERIAL PRIMARY KEY,
                brand VARCHAR(100) NOT NULL,
                model VARCHAR(100) NOT NULL
            )
        """)
    connection.commit()


def populate_cars_table(connection, cars):
    with connection.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO cars (brand, model) VALUES (%s, %s)",
            cars
        )
    connection.commit()


def get_all_cars(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, brand, model 
            FROM cars 
            ORDER BY brand ASC
        """)
        return cursor.fetchall()
# END
