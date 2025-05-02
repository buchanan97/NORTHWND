from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schema, crud, db

app = FastAPI()

# Dependency
def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.get("/customers/", response_model=list[schema.CustomerOut])
def read_customers(skip: int = 0, limit: int = 10, database: Session = Depends(get_db)):
    customers = crud.get_customers(database, skip=skip, limit=limit)
    return customers


import psycopg2

def connect_and_query(username, password):
    try:
        # Connect to the NorthWind database with your credentials
        conn = psycopg2.connect(
            dbname="NorthWind",
            user="northwind_user",   # The user created above
            password="nyit2001!!",
            host="localhost",        # Change if your DB is remote
            port="5432"
        )
        cur = conn.cursor()

        # Example: safely query customers by country (user input)
        user_input_country = input("Enter country to search customers: ")

        # Parameterized query to prevent SQL injection
        query = "SELECT customerid, companyname, contactname FROM customers WHERE country = %s;"
        cur.execute(query, (user_input_country,))

        results = cur.fetchall()
        for row in results:
            print(row)

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
     connect_and_query("northwind_user", "nyit2001!!")
