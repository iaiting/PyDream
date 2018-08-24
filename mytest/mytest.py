#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time

import asyncio

def now_time():
    nt = datetime.datetime.now()
    return nt

def fmt_time(nt=None):
    if not nt:
        nt = datetime.datetime.now()
    fmt_nt = nt.strftime('%Y-%m-%d %H:%M:%S')
    return fmt_nt


from tornado import gen
import random

async def do_something(num=1):
    print("Enter do_something : ")
    print("This number is : {0}".format(num))
 
    start_time = now_time()
    print("Start time : {0}".format(fmt_time(start_time)))


 

    wait_time = random.randint(1, 4)
    time.sleep(wait_time)
    end_time = now_time()
    print("End time : {0}".format(fmt_time(end_time)))

    print("总计花费的时间 : {0} 秒".format((end_time - start_time).seconds))
    print("")
    return {"id": num}

def mytest_001():
    c = do_something(2)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(c)



async def hello():
    print("Hello world!")
    await asyncio.sleep(1)
    print("Hello again!")




def mytest_004():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def main_mytest():
    # hello()
    mytest_001()
    # mytest_002()
    # mytest_003()
    # mytest_004()




################################################################################
if __name__ == '__main__':
    main_mytest()
