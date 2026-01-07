import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def batch_insert(connection, products):
    if not products:
        return
    
    data = [(p['name'], p['price'], p['quantity']) for p in products]
    
    with connection.cursor() as cursor:
        execute_values(
            cursor,
            """
            INSERT INTO products (name, price, quantity) 
            VALUES %s
            """,
            data,
            template="(%s, %s, %s)",
            page_size=100
        )
    connection.commit()


def get_all_products(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, price, quantity 
            FROM products 
            ORDER BY price DESC
        """)
        return cursor.fetchall()
# END
