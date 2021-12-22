"""
    → count

    → https://docs.python.org/2/library/datetime.html
"""

# declare
from datetime import datetime, timedelta

date = datetime(2021, 12, 20, 10, 53, 20)

# format (use directives)
print(date.strftime('%d/%m/%Y %H:%M:%S'))

# convert str in datetime
date = datetime.strptime('20/04/2021', '%d/%m/%Y')

# timestamp
date.timestamp()
datetime.fromtimestamp(date.timestamp())

# timedelta
date = date + timedelta(days=5, seconds=59)

# compare
date1 = datetime.strptime('20/04/2021 20:00:00', '%d/%m/%Y %H:%M:%S')
date2 = datetime.strptime('22/04/2021 21:00:00', '%d/%m/%Y %H:%M:%S')

print(date1.time())

difference = date2 - date1

print(difference)
print(difference.days)
print(difference.seconds)

# dates in portuguese brazil

from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
current_month = int(dt.strftime('%m'))
last_day_month = mdays[current_month]

# sábado, 13 de julho de 2019
format1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
format2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(format1, format2)
print(current_month, mdays[current_month])