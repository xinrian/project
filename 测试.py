import datetime
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.now(datetime.timezone.utc)
gree = dt_utcnow.strftime('%Y-%m-%d %H:%M:%S.%f %Z')
print(gree)

Y = gree[0:4]
M = gree[5:7]
D = gree[8:10]

h = gree[11:13]
m = gree[14:16]
s = gree[17:19]
print(Y,M,D,h,m,s)
