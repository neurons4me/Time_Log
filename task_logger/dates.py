from datetime import datetime, timedelta

# Supplies a list of dates for the current week starting on Monday
def latest_week_dates(formatted=False):
    today = datetime.today()

    monday = datetime.today() - timedelta(days=today.weekday())

    tuesday = monday + timedelta(days=1)
    wednesday = monday + timedelta(days=2)
    thursday = monday + timedelta(days=3)
    friday = monday + timedelta(days=4)
    saturday = monday + timedelta(days=5)
    sunday = monday + timedelta(days=6)

    if formatted:
        date_list = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
        new_date_list = []
        for item in date_list:
            new_date_list.append(item.strftime('%Y-%m-%d'))
        return new_date_list

    else:
        return [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

#TODO add function to calc latest complete week
def latest_complete_week():
    today =datetime.today()

    pass
