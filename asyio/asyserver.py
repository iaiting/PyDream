#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiohttp.web
import datetime
import random
import asyncio
async def handle(request):
    number = request.match_info.get('num', 'No Number')
    n = datetime.datetime.now().isoformat()

    delay = random.uniform(0, 3)
    await asyncio.sleep(delay)

    headers = {"content_type": "text/html", "delay": str(delay)}

    print("{}".format(n))
    text = 'Hello, ' + number
    print("{} delay: {}".format(n, delay))
    return aiohttp.web.Response(text=text, headers=headers)


def main():
    app = aiohttp.web.Application()
    app.router.add_get("/", handle)
    app.router.add_get("/{num}", handle)
    aiohttp.web.run_app(app)
if __name__ == '__main__':
    main()
