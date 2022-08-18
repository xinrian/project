cf_info = '''Disk /dev/sdb: 4000.8 GB, 4000787030016 bytes, 7814037168 sectors
Disk /dev/sda: 2012 MB, 2012774400 bytes, 3931200 sectors
Disk /dev/sdd: 30.8 GB, 30765219840 bytes, 60088320 sectors
Disk /dev/sdc: 30.8 GB, 30765219840 bytes, 60088320 sectors'''

cf_txt = open('test.txt')
cf = cf_txt.read()
print(cf)
if cf in cf_info:

    print('通过')
else:
    print('不通过')