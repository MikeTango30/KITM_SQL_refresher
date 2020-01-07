import sqlite3
# employee_id,
# first_name,
# last_name,
# email,
# phone_number,
# hire_date,
# job_id,
# salary,
# commission_pct,
# manager_id,
# department_id
db_name = "exercise.db"


def execute_select_query(query):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        rows = cursor.execute(query).fetchall()
        return rows
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        # noinspection PyUnboundLocalVariable
        connection.close()


def exercise_one():
    # 1. Write a query to display the names (first_name, last_name)
    # and salary for all employees whose salary
    # is not in the range $10,000 through $15,000.
    query = """SELECT first_name, last_name, salary 
                FROM employees 
                WHERE salary 
                NOT BETWEEN 10000 AND 15000"""
    print(execute_select_query(query))


def exercise_two():
    # 2. Write a query to display the names (first_name, last_name)
    # and department ID of all employees
    # in departments 30 or 100 in ascending alphabetical order by department ID.
    query = """SELECT first_name, last_name, department_id 
                FROM employees 
                WHERE department_id=30 OR department_id=100 
                ORDER BY department_id """
    print(execute_select_query(query))


def exercise_three():
    # 3. Write a query to display the names (first_name, last_name) and salary for all employees
    # whose salary is not in the range $10,000 through $15,000
    # and are in department 30 or 100.
    query = """SELECT first_name, last_name, salary
                FROM employees 
                WHERE salary NOT BETWEEN 10000 AND 15000 
                AND department_id=30 OR department_id=100 
                ORDER BY department_id"""
    print(execute_select_query(query))


def exercise_four():
    # 4. Write a query to display the first_name of all employees who have both an "b" and "c" in their first name.
    query = """SELECT first_name
                FROM employees 
                WHERE first_name LIKE '%b%' AND first_name LIKE '%c%'"""
    print(execute_select_query(query))


def exercise_five():
    # 5. Write a query to display the last name, job, and salary for all employees
    # whose job_id is IT_PROG or a SH_CLERK,
    # and whose salary is not equal to $4,500, $10,000, or $15,000
    query = """SELECT last_name, job_id, salary
                FROM employees 
                WHERE job_id = 'IT_PROG' OR job_id = 'SH_CLERK'"""
    print(execute_select_query(query))


def exercise_six():
    # 6. Write a query to display the last names of employees whose names have exactly 6 characters.
    query = """SELECT last_name
                FROM employees 
                WHERE first_name LIKE '______'"""
    print(execute_select_query(query))


def exercise_seven():
    # 7. Write a query to display the last names of employees having 'e' as the third character.
    query = """SELECT last_name
                FROM employees 
                WHERE first_name LIKE '__e%'"""
    print(execute_select_query(query))


exercise_one()
exercise_two()
exercise_three()
exercise_four()
exercise_five()
exercise_six()
exercise_seven()


