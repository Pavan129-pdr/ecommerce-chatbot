import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="ecommerce_chatbot",
        user="postgres",
        password="Pavan",
        host="localhost",
        port="5432"
    )
