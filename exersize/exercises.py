import sqlite3

db_name = "exercise.db"


def execute_select_query(query):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        rows = cursor.execute(query).fetchall()
        for row in rows:
            print(row)
        return rows
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        # noinspection PyUnboundLocalVariable
        connection.close()


# Part One
def exercise_one():
    # 1. Write a query to display the names (first_name, last_name)
    # and salary for all employees whose salary
    # is not in the range $10,000 through $15,000.
    query = """SELECT first_name, last_name, salary 
                FROM employees 
                WHERE salary 
                NOT BETWEEN 10000 AND 15000"""
    execute_select_query(query)


def exercise_two():
    # 2. Write a query to display the names (first_name, last_name)
    # and department ID of all employees
    # in departments 30 or 100 in ascending alphabetical order by department ID.
    query = """SELECT first_name, last_name, department_id 
                FROM employees 
                WHERE department_id=30 OR department_id=100 
                ORDER BY department_id """
    execute_select_query(query)


def exercise_three():
    # 3. Write a query to display the names (first_name, last_name) and salary for all employees
    # whose salary is not in the range $10,000 through $15,000
    # and are in department 30 or 100.
    query = """SELECT first_name, last_name, salary
                FROM employees 
                WHERE salary NOT BETWEEN 10000 AND 15000 
                AND department_id=30 OR department_id=100 
                ORDER BY department_id"""
    execute_select_query(query)


def exercise_four():
    # 4. Write a query to display the first_name of all employees who have both an "b" and "c" in their first name.
    query = """SELECT first_name
                FROM employees 
                WHERE first_name LIKE '%b%' AND first_name LIKE '%c%'"""
    execute_select_query(query)


def exercise_five():
    # 5. Write a query to display the last name, job, and salary for all employees
    # whose job_id is IT_PROG or a SH_CLERK,
    # and whose salary is not equal to $4,500, $10,000, or $15,000
    query = """SELECT last_name, job_id, salary
                FROM employees 
                WHERE (job_id = 'IT_PROG' OR job_id = 'SH_CLERK')
                AND (salary != 4500 AND salary != 10000 AND salary != 15000)"""
    execute_select_query(query)


def exercise_six():
    # 6. Write a query to display the last names of employees whose names have exactly 6 characters.
    query = """SELECT last_name
                FROM employees 
                WHERE LENGTH(first_name) = 6"""
    execute_select_query(query)


def exercise_seven():
    # 7. Write a query to display the last names of employees having 'e' as the third character.
    query = """SELECT last_name
                FROM employees 
                WHERE first_name LIKE '__e%'"""
    execute_select_query(query)


# Part Two
def exercise_1():
    # 1. Write a query to list the amount of jobs available in the employees table. ANSWER: 19.
    query = """SELECT COUNT(DISTINCT job_id)
                FROM employees"""
    execute_select_query(query)


def exercise_2():
    # 2. Write a query to get the total of salaries to pay.
    query = """SELECT SUM(salary)
                FROM employees"""
    execute_select_query(query)


def exercise_3():
    # 3. Write a query to get the minimum salary from employees table.
    query = """SELECT salary
                FROM employees ORDER BY salary LIMIT 1"""
    execute_select_query(query)


def exercise_4():
    # 4. Write a query to get the highest salary of an employee.
    query = """SELECT salary
                FROM employees ORDER BY salary DESC LIMIT 1"""
    execute_select_query(query)


def exercise_5():
    # 5. Write a query to get average salary and number of employees working  in department 90.
    query = """SELECT AVG(salary), COUNT(employee_id)
                FROM employees 
                WHERE department_id = 90"""
    execute_select_query(query)


def exercise_6():
    # 6. Write a query to get the highest, lowest, sum and average salary of all employees.
    query = """SELECT MAX(salary), MIN(salary), SUM(salary), AVG(salary)
                FROM employees"""
    execute_select_query(query)


def exercise_7():
    # 7. Write a query to get the number of employees with the same job.
    query = """SELECT COUNT(employee_id)
                FROM employees
                GROUP BY job_id"""
    execute_select_query(query)


def exercise_8():
    # 8. Write a query to get the difference between the highest and lowest salaries.
    query = """SELECT MAX(salary) - MIN(salary)
                FROM employees"""
    execute_select_query(query)


def exercise_9():
    # 9. Write a query to get the department ID and the total salary payable in each department.
    query = """SELECT department_id, SUM(salary)
                FROM employees
                GROUP BY department_id"""
    execute_select_query(query)


def exercise_10():
    # 10. Write a query to get the average salary for each job ID excluding programmers.
    query = """SELECT AVG(salary)
                FROM employees
                WHERE NOT job_id = 'IT_PROG'
                GROUP BY job_id"""
    execute_select_query(query)


def exercise_11():
    # 11. Write a query to find the manager ID and the salary of the lowest paid employee for that manager.
    query = """CREATE VIEW IF NOT EXISTS lowest_salary_by_manager AS
                SELECT manager_id, MIN(salary)
                FROM employees
                GROUP BY manager_id"""
    execute_select_query(query)
    execute_select_query("SELECT * FROM lowest_salary_by_manager")


# PART THREE
def exercise_3_1():
    # 1. Write a query to find the names (first_name, last_name) and salaries of the employees
    # who have a higher salary than the employee whose last_name='Bull'.
    query = """SELECT first_name, last_name, salary FROM employees
                WHERE salary > (SELECT salary FROM employees WHERE last_name = 'Bull')"""
    execute_select_query(query)


def exercise_3_2():
    # 2. Write a query to find the names (first_name, last_name) of the employees who are managers
    query = """SELECT first_name, last_name FROM employees
                WHERE employee_id IN (
                SELECT manager_id FROM employees)"""
    execute_select_query(query)


def exercise_3_3():
    # 3. Write a query to find the names (first_name, last_name), the salary of the employees
    # whose salary is greater than the average salary
    query = """SELECT first_name, last_name, salary FROM employees
                WHERE salary > (SELECT AVG(salary) FROM employees)"""
    execute_select_query(query)


def exercise_3_4():
    # 4. Write a query to find the names (first_name, last_name), the salary of the employees
    # whose salary is equal to the minimum salary for their job grade.
    # Tables: employees, jobs.
    query = """SELECT first_name, last_name, salary FROM employees
                WHERE salary = (SELECT min_salary FROM jobs WHERE job_id = employees.job_id)"""
    execute_select_query(query)


def exercise_3_5():
    # 5. Write a query to find the names (first_name, last_name), the salary of the employees
    # who earn more than the average salary
    # and who works in any of the IT departments.
    # Tables: employees, departments
    query = """SELECT first_name, last_name, salary FROM employees
                WHERE salary > (SELECT AVG(salary) FROM employees) 
                AND department_id IN (SELECT department_id FROM departments WHERE depart_name LIKE 'IT%')"""
    execute_select_query(query)


def exercise_3_6():
    # 6. Write a query to get 3 maximum salaries.
    # Tables: employees
    query = """SELECT salary FROM employees ORDER BY salary DESC LIMIT 3"""
    execute_select_query(query)


def exercise_3_7():
    # 7. Write a query to find the names (first_name, last_name) of the employees
    # who have a manager who works for a department based in the United States.
    # Tables: employees, departments, locations

    # query1 = """SELECT first_name, last_name FROM employees
    #                   WHERE manager_id IN (
    #                   SELECT manager_id FROM departments WHERE location_id IN (
    #                   SELECT location_id FROM locations WHERE country_id = 'US'))"""

    query = """SELECT first_name, last_name FROM employees
                WHERE manager_id IN (
                SELECT employee_id FROM employees WHERE department_id IN ( 
                SELECT department_id FROM departments WHERE location_id IN (
                SELECT location_id FROM locations WHERE country_id = 'US')))"""
    execute_select_query(query)


# execute_select_query("PRAGMA table_info (employees)")

# # PART ONE
# exercise_one()
# exercise_two()
# exercise_three()
# exercise_four()
# exercise_five()
# exercise_six()
# exercise_seven()

# # PART TWO
# exercise_1()
# exercise_2()
# exercise_3()
# exercise_4()
# exercise_5()
# exercise_6()
# exercise_7()
# exercise_8()
# exercise_9()
# exercise_10()
# exercise_11()

# PART THREE
# exercise_3_1()
# exercise_3_2()
# exercise_3_3()
# exercise_3_4()
# exercise_3_5()
# exercise_3_6()
# exercise_3_7()

# 3_4 CHECK:
# execute_select_query("SELECT job_id, MIN(salary) FROM employees GROUP BY job_id ORDER BY job_id")
# execute_select_query("SELECT job_id, min_salary FROM jobs ORDER BY job_id")

# 3_7 CHECK | managers in US
# execute_select_query("""SELECT DISTINCT manager_id FROM departments
#                         WHERE location_id IN (
#                         SELECT location_id FROM locations
#                         WHERE country_id = 'US') ORDER BY manager_id""")
# execute_select_query("SELECT first_name, last_name FROM employees WHERE manager_id = 200")

# if list1 == list3:
#     print("yes")

# for record in list1:
#     if record in list2:
#         print("yes")
#     else:
#         print(record)
#         print("no")

# execute_select_query("PRAGMA table_info (departments)")
# execute_select_query("SELECT * FROM departments")
# execute_select_query("PRAGMA table_info (employees)")
# execute_select_query("SELECT * FROM employees")
# execute_select_query("PRAGMA table_info (locations)")
# execute_select_query("SELECT * FROM locations")
# execute_select_query("SELECT * FROM employees WHERE last_name = 'Mavris'")

# EMPLOYEES
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
# Avg_Salary

# JOBS
# job_id
# job_title
# min_salary
# max_salary

# DEPARTMENTS
# department_id,
# depart_name,
# manager_id,
# location_id

# LOCATIONS
# location_id
# street_address
# postal_code
# city
# state_province
# country_id

# JOB HISTORY
# employee_id
# start_date
# end_date
# job_id
# department_id


# PART FOUR
def exercise_4_1():
    # 1.Write a query to get the department name and number of employees in the department
    # Tables: employees, departments
    query = """SELECT depart_name, COUNT(employee_id) 
                                FROM departments 
                                JOIN employees 
                                USING(department_id) 
                                GROUP BY depart_name"""
    execute_select_query(query)


def exercise_4_2():
    # 2.Write a query to display the department ID, department name, and manager first name.
    # Tables: employees, departments
    query = """SELECT departments.department_id, departments.depart_name, first_name 
                                FROM departments 
                                JOIN employees 
                                ON departments.manager_id = employees.employee_id 
                                GROUP BY depart_name 
                                ORDER BY departments.department_id  
                                """
    execute_select_query(query)


def exercise_4_3():
    # 3. Write a query to display the department name, manager name, and city.
    # Tables: employees, departments, locations
    query = """SELECT depart_name, first_name, city 
                                FROM departments 
                                JOIN employees 
                                ON departments.manager_id = employees.employee_id
                                JOIN locations
                                ON departments.location_id = locations.location_id 
                                GROUP BY depart_name 
                                ORDER BY departments.department_id  
                                """
    execute_select_query(query)


def exercise_4_4():
    # 4.Write a query to display the job history
    # that was done by any employee who is currently drawing more than 10000 of salary.
    # Tables: employees, job_history
    query = """SELECT * FROM job_history JOIN employees USING(employee_id) WHERE salary > 10000"""
    execute_select_query(query)


def exercise_4_5():
    # 5.Write a query to display the job title and average salary of employees.
    # Tables: employees, jobs
    query = """SELECT job_title, AVG(salary) FROM jobs 
                                            JOIN employees 
                                            USING(job_id) GROUP BY job_title"""
    execute_select_query(query)


def exercise_4_6():
    # 6. Write a query to find the employee ID, job title number of days between ending date and starting date
    # for all jobs in department 90 from job history.
    # Tables:job_history, jobs
    query = """SELECT employee_id, job_title, end_date - start_date FROM job_history
                                    NATURAL JOIN jobs 
                                    WHERE job_history.department_id = 90"""
    execute_select_query(query)


def exercise_4_7():
    # 7. Write a query to find the names (first_name, last_name) and hire date of the employees
    # who were hired after employee with last name 'Jones'.
    # Tables: employees
    query = """SELECT employees.first_name, employees.last_name, employees.hire_date FROM employees
                                    JOIN employees jones
                                    ON jones.last_name = 'Jones'
                                    WHERE employees.hire_date > jones.hire_date"""
    execute_select_query(query)


# exercise_4_1()
# exercise_4_2()
# exercise_4_3()
# exercise_4_4()
# exercise_4_5()
# exercise_4_6()
# exercise_4_7()
