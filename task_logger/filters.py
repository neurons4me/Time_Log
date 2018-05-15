from task_logger.models import Time_record


def all_for_user(user):
    # all_logs = Time_record.objects.all()
    # print(all_logs)
    return Time_record.objects.filter(user_id=user)

def current_entry(user):
    all_by_user = all_for_user(user)
    only_incomplete = all_by_user.exclude(activity_end__isnull=False).filter(clocked_in=True)

    return only_incomplete
