import re
import time

data_str = '''[SAT 05/07/2022]
［13:44:14]'''
time_list = []
for i in range(len(data_str)):
    # 去除空格和准确率保留时间信息
    time_list.append(''.join(re.findall('[0-9]', data_str[i].strip().replace(' ', '')[4:])))
    print(time_list)

# 加工，生成字符串时间戳
time_str = (time_list[0][4:] + '-' + time_list[0][0:2] + '-' + time_list[0][2:4])
time_str = (time_str + ' ' + time_list[1][0:2] + ':' + time_list[1][2:4] + ':' + time_list[1][4:])

print(time_str)

# 生成世界时间戳
timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
timestamp = int(time.mktime(timeArray))

# 当前国际时间戳
sys_stamp = int(time.time())

if timestamp - 120 < sys_stamp < timestamp + 120:
    pt_status = 0
else:
    pt_status = -1
