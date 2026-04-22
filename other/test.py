import psycopg2
from psycopg2.extras import RealDictCursor 

try : 
    conn = psycopg2.connect(host = "localhost", database = "fastapi", user = "postgres", password = "2006", cursor_factory=RealDictCursor)
    cursor = conn.cursor() 
    print("Database connection was successful")
except Exception as error : 
    print("Connecting to Database failed")
    print("Error : ", error)