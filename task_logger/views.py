from django.shortcuts import render
from task_logger.models import Time_record
from task_logger.filters import all_for_user, current_entry
from django.utils import timezone
from task_logger.calc import day_total_duration, format_duration_hhmm

# Create your views here.


def index(request):
    #TODO 1. fix the issue of pottentially clocking out on multiple open entries
    #TODO 2. add error logging to extra open entries
    #TODO 3. add rudementary reports
    #TODO 4. add approvals and editing
    #TODO 5. add 'clocked in since xx:xx' to template
    #TODO 6. add user authentication
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

def reports(request):

    context = {'total_today': format_duration_hhmm(day_total_duration('amcdaniel', 2018, 5, 15))}
    return render(request, 'task_logger/Reports.html' ,context)


def approvals(request):
    pass