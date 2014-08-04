import datetime

t=datetime.time(1, 2, 3)
print t
print 'hour       :', t.hour
print 'minute     :', t.minute
print 'second     :', t.second
print 'microsecond:', t.microsecond
print 'tzinfo     :', t.tzinfo

today = datetime.date.today()
print today
print 'ctime      :', today.ctime()
tt = today.timetuple()
print 'tuple      : tm_year    =', tt.tm_year


