import datetime

# INPUT DATE IN FORMAT DD-MM-YYYY


def what_age(input_date):

    today = datetime.date.today()

    day, month, year = int(input_date[0:2]), int(
        input_date[3:5]), int(input_date[6:])

    user_date = datetime.date(year, month, day)
    age = today.year - user_date.year

    if today.month > user_date.month:
        age = age
    elif today.month == user_date.month and today.day >= user_date.day:
        age = age
    else:
        age -= 1

    print(age)
    return age


what_age('01-01-1993')
