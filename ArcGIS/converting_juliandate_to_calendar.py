import datetime

year = '2018'
def reclass(y):
    date = datetime.datetime.strptime(str(y), '%j').date()
    return date.strftime('%d/%m/' + year)