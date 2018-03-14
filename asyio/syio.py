#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

URL = "http://127.0.0.1:8080"


def http_get():
    ret = requests.get('http://httpbin.org/get')
    return ret


def http_get2():
    for i in range(4):
        ret = requests.get("{}/{}".format(URL, i))
        print(ret.text)


def http_get3(num):
    for i in range(num):
        ret = requests.get("{}/{}".format(URL, i))
        delay = ret.headers.get("DELAY")
        d = ret.headers.get("DATE")
        print("{}:{} delay {}".format(d, ret.url, delay))


def main():
    # result = http_get()
    # print(result)
    # http_get2()
    http_get3(10)
if __name__ == '__main__':
    main()
