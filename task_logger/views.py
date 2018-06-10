from django.shortcuts import render
from task_logger.models import Time_record
from task_logger.filters import all_for_user, current_entry
from django.utils import timezone
from task_logger.calc import day_total_duration, format_duration_hhmm
from django.contrib.auth.decorators import login_required
from task_logger.dates import latest_week_dates

# Create your views here.

@login_required
def index(request):
    #TODO 1. fix the issue of pottentially clocking out on multiple open entries
    #TODO 2. add error logging to extra open entries
    #TODO 3. add rudementary reports
    #TODO 4. add approvals and editing
    #TODO 5. add 'clocked in since xx:xx' to template
    #TODO 6. add meal in/meal out

    curent_user = request.user.username

    # if no incomplete entries display the 'start button'
    if len(current_entry(curent_user)) == 0:
        page_mode = 'task_logger/Start-mode.html'
        # TODO for meal in/out need to add button for 'start meal break'

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


@login_required
def reports(request):
    curent_user = request.user.username
    date_list = []
    for day in latest_week_dates():
        date_list.append(format_duration_hhmm(day_total_duration(curent_user, day.year, day.month, day.day)))
        #TODO add dates to context dict so we can display that was well
        #TODO include this simple report on main clock in/clock out views
        #TODO refactor date_list name... it is not clear what it is from the name
        #TODO now that we have the date for the latest complete week we can generate some reports for that week
    today = timezone.now()
    context = {'total_today': format_duration_hhmm(day_total_duration(curent_user, today.year, today.month, today.day)),
               'date_list': date_list,
               'latest_dates_list' : latest_week_dates(formatted=True)
               }
    return render(request, 'task_logger/Reports.html' ,context)


@login_required
def approvals(request):
    pass


@login_required
def user_creation(request):
    registered = False
