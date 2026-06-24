import sqlite3
import pandas as pd

DB_NAME = 'company.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """
    Table creation in company.db database.
    """
    conn = get_connection()

    cursor = conn.cursor()

    # Employee table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            employee_id TEXT PRIMARY_KEY,
            employee_name TEXT NOT NULL,
            designation TEXT NOT NULL, 
            department TEXT NOT NULL,
            email_id TEXT UNIQUE,
            phone_no TEXT
            )
    """)

    # Ticket table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket(
            ticket_id TEXT PRIMARY_KEY,
            issue TEXT NOT NULL,
            created_at TEXT NOT NULL
            )
    """)

    conn.commit()
    conn.close()

    return "Tables created!"


def insert_data():
    """
    Data insertion in the the employee table for the company database.
    """

    conn = get_connection()
    employees_df = pd.read_csv('employees.csv')
    employees_df.to_sql(
        'employees',
        conn,
        if_exists='append',
        index=False)

    conn.close()

    return "Data loaded into employees table"

def data_test():
    """
    Data check for the employee table.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from employees limit 5")

    rows = cursor.fetchall()

    for row in rows:
        print(dict(row))

    conn.close()

if __name__ == "__main__":
    # create_tables()
    # insert_data()
    data_test()