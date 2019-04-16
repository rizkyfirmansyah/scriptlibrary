from datetime import datetime
def redate(a):
    if (len(a) == 13):
        ts = int(a[0:10])
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
    elif (len(a) == 12):
        ts = int(a[0:9])
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
    else:
        return None
	
# if the date type is float / double
from datetime import datetime
def redate(a):
    if (a != 0):
        ts = int(a/1000)
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
    else:
        return None
		

# Left as null if you find the number below		
# -2209161600000 = 12/30/1899
# change to 12/30/1998
