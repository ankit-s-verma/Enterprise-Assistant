from app.database.database import get_connection
import warnings
warnings.filterwarnings('ignore')

def get_employee_by_id(employee_id) -> dict | None:
    """
    Returns the emloyee details using the employee id from the employees table. 
    Response is in JSON format. eg - {'emp_id' : '1234', 'emp_name' : 'Tony Brown'} 
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE employee_id = ?",
        (employee_id,)
    )

    employee = cursor.fetchone()
    

    conn.close()

    return dict(employee) if employee else None

def get_employee_by_name(employee_name) -> dict | None:
    """
    Returns the emloyee details using the employee name from the employees table. 
    Response is in JSON format. eg - {'emp_id' : '1234', 'emp_name' : 'Tony Brown'} 
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE LOWER(employee_name) = LOWER(?)",
        (employee_name,)
    )

    employee = cursor.fetchone()

    conn.close()

    return dict(employee) if employee else None

if __name__ == "__main__":
    print(get_employee_by_name('Benjamin Moore'))
    print(get_employee_by_id('E115'))