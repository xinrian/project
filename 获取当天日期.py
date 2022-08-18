import datetime
test = 'DMI /BT '
now_time = datetime.datetime.now()
today = datetime.datetime.now().strftime('%m/%d/%Y')
all = test+today
print(all)