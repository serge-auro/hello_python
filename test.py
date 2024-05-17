from datetime import datetime, timedelta

today = datetime.now()
#if period == 'Текущая неделя':
start_of_week = today - timedelta(days=today.weekday())  # начало текущей недели (понедельник)
start_of_month = today.replace(day=1)  # начало текущего месяца
start_date = start_of_month.strftime('%Y-%m-%d')
start_date2 = start_of_week.strftime('%Y-%m-%d')
print("start_of_week=", start_of_week)
print("start_date=", start_date)
print("start_date=", start_date2)

if 1==2: pass
elif period == 'Прошедшая неделя':
    start_of_last_week = today - timedelta(days=today.weekday() + 7)  # начало прошлой недели
    end_of_last_week = start_of_last_week + timedelta(days=6)  # конец прошлой недели
    start_date = start_of_last_week.strftime('%Y-%m-%d')
    end_date = end_of_last_week.strftime('%Y-%m-%d')
elif period == 'Текущий месяц':
    start_of_month = today.replace(day=1)  # начало текущего месяца
    start_date = start_of_month.strftime('%Y-%m-%d')
elif period == 'Прошедший месяц':
    start_of_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)  # начало прошлого месяца
    end_of_last_month = (today.replace(day=1) - timedelta(days=1))  # конец прошлого месяца
    start_date = start_of_last_month.strftime('%Y-%m-%d')
    end_date = end_of_last_month.strftime('%Y-%m-%d')