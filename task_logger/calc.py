from task_logger.filters import all_on_date_for_user


def duration(start_time, end_time):
    duration = end_time - start_time
    return duration.seconds


def day_total_duration(user, year, month, day):
   filter_results = all_on_date_for_user(user, year, month, day)
   total_duration = 0
   for entry in filter_results:
       total_duration += duration(entry.activity_start, entry.activity_end)
   return total_duration

def format_duration_hhmm(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) / 60

    return str('%ih %im' % (hours, minutes))

