import mysql.connector
from config import DATABASE_CONFIG

def connect():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG["host"],
            port=DATABASE_CONFIG["port"],
            user=DATABASE_CONFIG["user"],
            password=DATABASE_CONFIG["password"],
            database=DATABASE_CONFIG["database"]
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

def load(data):
    connection = connect()
    if not connection:
        print("Failed to connect to the database")
        return False

    cursor = connection.cursor()
    for product in data:
        try:
            cursor.execute(
                "INSERT INTO tb_products (name_product, price, description_product, category, image, rate, count) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    product.get("title"),
                    product.get("price"),
                    product.get("description"),
                    product.get("category"),
                    product.get("image"),
                    product.get("rate"),
                    product.get("count"),
                ),
            )

            if cursor.rowcount > 0:
                print(f"Inserted product: {product['title']}")
                
        except mysql.connector.Error as err:
            print(f"Error inserting data into the database: {err}")

    connection.commit()
    cursor.close()
    connection.close()
    return True


def query_duplicates(title):
    connection = connect()
    if not connection:
        print("Failed to connect to the database")
        return False

    cursor = connection.cursor()
    cursor.execute("""select name_product
                        from tb_products""")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    if rows:
        for row in rows:
            if row[0] == title:
                return True, rows

    # No matching title found — return False and the fetched rows (empty or full list)
    return False, rows