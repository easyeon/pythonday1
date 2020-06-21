# -*- coding:utf-8 -*-
#!/usr/bin/python3
import _thread

import time

# 定义线程调用函数
def echo_name(tag,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s" % ( tag,time.ctime(time.time()) ))
#创建2个线程
try:
    _thread.start_new_thread(echo_name,("thread_1",2))
    _thread.start_new_thread(echo_name,("thread_2",5))
except:
    print("error:无法启动线程")
#死循环
while 1:
    pass

