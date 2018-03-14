#!/usr/bin/env python3
import asyncio
import time


async def work(i, t):
    print('******work[%i], runtime[%f]' % (i, t))
    await asyncio.sleep(2)


async def test_server(num):
    print('*******: begin: ', num)
    for i in range(num):
        await work(i, 2)


def main():
    tasknum = 10
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_server(tasknum))
    loop.close()

if __name__ == '__main__':
    main()
