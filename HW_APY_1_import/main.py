from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt
import netflix

if __name__ == '__main__':
    print(dt.datetime.now().strftime('%d-%m-%Y %H:%M'))
    calculate_salary()
    get_employees()