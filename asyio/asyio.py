#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import aiohttp

# URL = "http://httpbin.org/headers"
URL = "http://127.0.0.1:8080"

async def http_get(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as response:
            delay = response.headers.get("DELAY")
            date = response.headers.get("DATE")
            print("{}:{} with delay {}".format(date, response.url, delay))
            return await response.read()


async def run(loop, num):
    tasks = []
    for i in range(num):
        task = asyncio.ensure_future(http_get("{}/{}".format(URL, i)))
        tasks.append(task)
        response = await asyncio.gather(*tasks)

        print(response)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(http_get(URL))
    loop.close()


def main2():
    tasks = []
    for i in range(10):
        url = "{}/{}".format(URL, i)
        task = asyncio.ensure_future(http_get(url))
        tasks.append(task)
        # print(url)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def main3():
    await responses number = 10000
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(loop, 5))
    loop.run_until_complete(future)
    loop.close()

if __name__ == '__main__':
    # main()
    # main2()
    main3()
