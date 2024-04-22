from datetime import date
from application import salary
from application.db import people
from calendar import month


if __name__ == '__main__':
    print(salary.calculate_salary(0, 0))
    print(people.get_employees('Name', 'Ivan'))
    today = date.today() 
    print(today.day, today.month, today.year)