## Converting Day of Year to date-time format like DD-MM-YYYY. The input type has to be integer.
## It wouldn't work if you have double type. Best you add new integer field and converted from that.

import datetime

year = '2018'
def reclass(y):
    date = datetime.datetime.strptime(str(y), '%j').date()
    return date.strftime('%d/%m/' + year)