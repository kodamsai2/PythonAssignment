from datetime import datetime, timedelta

def getDateNDaysBefore(date, n):
    DateObject = datetime.strptime(date, '%y-%m-%d')
    BeforeDate = DateObject - timedelta(days=n)
    return BeforeDate.strftime('%y-%m-%d')

print(getDateNDaysBefore('16-12-10', 11))