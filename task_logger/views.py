from django.shortcuts import render
from task_logger.models import Time_record
from task_logger.filters import all_for_user, current_entry
from django.utils import timezone
# Create your views here.


def index(request):
    #check for current userID
    curent_user = 'amcdaniel'

    #query all entries for current userID
    all_user_entries = all_for_user(curent_user)

    #check if all entries are marked as complete
    # for entry in all_user_entries:
    #     if entry.activity_end.__isnull:
    #         print('I should display the clock out button')
       #if an in progress entry found display the clock out button via render_context dictionary

    # if no incomplete entries display the 'start button'
    if len(current_entry(curent_user)) == 0:
        print('DISPLAY START')
        page_mode = 'task_logger/Start-mode.html'

    else:
        page_mode = 'task_logger/Stop-mode.html'

    #on start button press: create a new entry and datetime stamp activity_start
    if 'start_button' in request.POST:
        Time_record.objects.create(activity_start=timezone.localtime(), user_id=curent_user, clocked_in=True)
        page_mode = 'task_logger/Stop-mode.html'

    #on stop_button press: complete entry
    if 'stop_button' in request.POST:
        entry_to_complete = current_entry(curent_user)
        for entry in entry_to_complete:

            entry.activity_end = timezone.localtime()
            entry.clocked_in = False
            entry.save()
        page_mode = 'task_logger/Start-mode.html'

    return render(request, page_mode)