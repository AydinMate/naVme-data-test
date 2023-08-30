import calendar

date = "2022-10-13"

year, month, day = date.split("-")

month_name = calendar.month_name[int(month)]

print(month_name)