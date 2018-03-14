#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


async def print_message():
    while True:
        print("Just printing a new message in 3 seconds:")
        await asyncio.sleep(3)


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(print_message())
    finally:
        loop.close()

if __name__ == '__main__':
    main()
