from task_logger.models import Time_record
from datetime import datetime

def all_for_user(user):
        return Time_record.objects.filter(user_id=user)

def current_entry(user):
    all_by_user = all_for_user(user)
    only_incomplete = all_by_user.exclude(activity_end__isnull=False).filter(clocked_in=True)

    return only_incomplete

def all_on_date_for_user(user, year, month, day):

    return Time_record.objects.filter(user_id=user, activity_end__year = year, activity_end__month= month, activity_end__day= day)