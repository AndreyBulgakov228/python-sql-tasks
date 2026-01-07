import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def get_order_sum(connection, month):
    result_lines = []
    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                c.customer_name,
                SUM(o.total_amount) as total_sum
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            WHERE EXTRACT(MONTH FROM o.order_date) = %s
            GROUP BY c.customer_id, c.customer_name
            ORDER BY c.customer_name  -- Сортировка по имени!
        """, (month,))
        
        for customer_name, total_sum in cursor.fetchall():
            if total_sum % 1 == 0:
                total_sum = int(total_sum)
            
            result_lines.append(f"Покупатель {customer_name} совершил покупок на сумму {total_sum}")
    
    return '\n'.join(result_lines)
# END
