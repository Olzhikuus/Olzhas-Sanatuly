import datetime
now = datetime.datetime.now()
yestr = now - datetime.timedelta(days=1)
tomrw = now + datetime.timedelta(days=1)
print("Yesterday:",yestr)
print("Today:",now)
print("Tomorrow:",tomrw)