from datetime import datetime, timedelta

def CheckDateRange(from_date, to_date, difference):
    FromDateObj = datetime.strptime(from_date, '%y-%m-%d')
    ToDateObj = datetime.strptime(to_date, '%y-%m-%d')
    DateDifference = FromDateObj - ToDateObj
    if DateDifference <= timedelta(days=difference):
        return True
    else:
        return False

print(CheckDateRange('21-04-01', '21-04-05', 5))