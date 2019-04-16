## Converting Day of Year to date-time format like DD-MM-YYYY. The input type has to be integer.
## It wouldn't work if you have double type. Best you add new integer field and converted from that.

"""
A coverage or shapefile stores dates in a date field with this format: yyyy-mm-dd
If you need to change how ArcMap displays date formats, you can access the Region and Language settings through your system's Control Panel.

The format for date fields in ArcMap is mm/dd/yyyy hh:mm:ss and a specification of AM or PM

References
http://desktop.arcgis.com/en/arcmap/10.3/manage-data/tables/fundamentals-of-date-fields.htm

http://desktop.arcgis.com/en/arcmap/latest/extensions/production-mapping/custom-date-formats.htm

https://www.journaldev.com/23365/python-string-to-datetime-strptime
"""

import datetime

year = '2019'
def reclass(y):
    date = datetime.datetime.strptime(str(y), '%j').date()
    return date.strftime(year + '-%m-%d')