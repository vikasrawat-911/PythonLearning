import datetime

t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"
dateT1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
dateT2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
print(dateT1)
print(dateT2)
diff = (dateT1-dateT2).total_seconds()
print(diff)