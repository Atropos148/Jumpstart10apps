import datetime


def print_header():
    print('---------------------------')
    print('    BIRTHDAY APP')
    print('---------------------------')


def get_birthday_date():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))

    birth_day = datetime.date(year, month, day)
    return birth_day


def calculate_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_result(days):
    if days < 0:
        print(f'You had your birthday {-days} days ago this year.')
    elif days > 0:
        print(f'Your birthday is in {days} days!')
    else:
        print('Happy birthday!')


def main():
    print_header()
    bday = get_birthday_date()
    today = datetime.date.today()
    number_of_days = calculate_days_between_dates(bday, today)
    print_result(number_of_days)


main()
