from datetime import datetime, timedelta

# Supplies a list of dates for the current week starting on Monday
def latest_week_dates():
    today = datetime.today()

    monday: datetime = datetime.today() - timedelta(days=today.weekday())

    tuesday = monday + timedelta(days=1)
    wednesday = monday + timedelta(days=2)
    thursday = monday + timedelta(days=3)
    friday = monday + timedelta(days=4)
    saturday = monday + timedelta(days=5)
    sunday = monday + timedelta(days=6)

    return [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

#TODO add function to calc latest complete week