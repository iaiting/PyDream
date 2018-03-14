#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading


@asyncio.coroutine
def hello(i):

    print("testing [{}:{}] start at [{}]".format(hello.__name__, i, threading.currentThread()))
    r = yield from asyncio.sleep(3)
    print("testing [{}:{}] end at [{}]".format(hello.__name__, i, threading.currentThread()))

# async 新语法，不在使用 @asyncio.coroutine和yield from

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


def test1():
    print("this is: ", test1.__name__)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()


def test2(num):
    tasks = []
    for i in range(num):
        tasks.append(hello(i))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print("this end:", test2.__name__)


def test3():
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    loop.close()
    print("this end:", test3.__name__)


def main():
    # test1()
    # test2(100)
    test3()
if __name__ == '__main__':
    main()
