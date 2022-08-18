import os

print(os.getcwd())  # 获取当前工作路径

print(os.listdir())  # 返回指定路径下文件和文件夹的列表

print(os.walk('远程登录'))  # 传入一个路径 获取每个文件夹下面的文件夹及文件列表

print(os.path.exists('远程登录'))  # 判断某个文件存在不存在 布尔值

print(os.makedirs('test1'))  # 递归生成文件夹

print(os.rmdir('test3'))  # 删除文件夹

print(os.mkdir('test3'))  # 创建一个文件夹

print(os.path.join('/test'))  # 路径拼接

print(os.path.split('te'))  # 路径切分

print(os.path.dirname('test'))  # 返回文件的绝对路径

print(os.path.basename('test'))  # 返回绝对路径下的文件名

print(os.path.isdir('test'))  # 判断是否是文件夹

print(os.path.isfile('当天日期.py'))  #判断是否是文件

print(os.sep)  # 返回当前操作系统的路径分隔符

print(os.path.getsize('魔法方法.py'))  # 返回当前文件的大小

