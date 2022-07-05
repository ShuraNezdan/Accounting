from application.salaty import calculate_salary
from application.db.people import get_emplotess
from datetime import datetime as da



def main():
    calculate_salary()
    get_emplotess()
    date_now = da.now().timetuple()
    print(f'Запуск программы прошел: {date_now[2]}-{date_now[1]}-{date_now[0]}')
    


if __name__ == '__main__':
    main()
