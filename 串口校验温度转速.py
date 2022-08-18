import re

bios = '''Aptio Setup Utility - Copyright (C) 2019 American
Megatrends, Inc. 
 Advanced 
/----------------------------------------------------+--
-----------------------\
| Pc Health Status | 
|
| | 
|
| System temperature : +37 .C | 
|
| CPU temperature : +52 .C | 
|
| Slot temperature : +34 .C | 
|
| CPU Fan Speed : 8385 RPM | 
|
| System Fan Speed : 7988 RPM | 
|
| Slot Fan Speed : 6279 RPM | 
|
| CPUVCORE : +1.256 V | 
|
| +V1P8 (1.8V) : +1.792 V |--
-----------------------|
| VDIMM (1.35V) : +1.360 V |>
<: Select Screen |
| +VDDCR_APU_NB : +0.800 V |^
v: Select Item |
| (0.7V~1.3V) |En
ter: Select |
| +12V : +11.880 V |+/
-: Change Opt. |
| +5V : +4.961 V |F
1: General Help |
| +3.3V : +3.321 V |F
2: Previous Values |
| |F
3: Optimized Defaults |
| |F
4: Save & Exit |
| |ES
C: Exit |
\----------------------------------------------------+--
-----------------------/
 Version 2.17.1246. Copyright (C) 2019 American M
egatrends, Inc. '''

sys_tem_re = 'System temperature.{9}'
spu_tem_re = 'CPU temperature.{9}'
slot_tem_re = 'Slot temperature.{9}'

cpu_fun_re = 'CPU Fan Speed.{11}'
cyc_fun_re = 'System Fan Speed.{11}'
slot_fun_re = 'Slot Fan Speed.{11}'

sys_tem = re.findall(sys_tem_re, bios)[0][22:25]
spu_tem = re.findall(spu_tem_re, bios)[0][19:22]
slot_tem = re.findall(slot_tem_re, bios)[0][20:23]

cpu_fun = re.findall(cpu_fun_re,bios)[0][16:21]
cyc_fu = re.findall(cyc_fun_re,bios)[0][19:23]
slot_fun = re.findall(slot_fun_re,bios)[0][17:22]

print(sys_tem,spu_tem,slot_tem,cpu_fun,cyc_fu,slot_fun)

temlist = [sys_tem, spu_tem, slot_tem]
fun_list = [cpu_fun, cyc_fu, slot_fun]

for i in temlist :
    if 30 < int(i) < 55:
        print('成功')
    else:
        print('停止')
for j in fun_list:
    if 6000 < int(j) < 8500:
        print('成功')
    else:
        print('停止')