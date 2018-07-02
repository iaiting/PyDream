#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xtime

################################################################################
#
# Author		: iaiting
#
################################################################################

G_ERRO = '\033[31m%s\033[0m' % ('ERRO')
G_INFO = '\033[32m%s\033[0m' % ('INFO')
G_WARN = '\033[33m%s\033[0m' % ('WARN')

################################################################################
def console_log(level, msg):
    if level == "INFO":
        log_info(msg)

    elif level == "WARN":
        log_warn(msg)

    elif level == "ERRO":
        log_erro(msg)

    else:
        pass

# [2018-06-28 12:00:00][INFO] test log
################################################################################
def log_info(msg):
    print("[%s][%s] %s" % (xtime.Get_Ymdhms(), G_INFO, msg))

################################################################################
def log_warn(msg):
    print("[%s][%s] %s" % (xtime.Get_Ymdhms(), G_WARN, msg))

################################################################################
def log_erro(msg):
    print("[%s][%s] %s" % (xtime.Get_Ymdhms(), G_ERRO, msg))

################################################################################
def _xlog(fmt_msg):
    print(fmt_msg)

################################################################################

def main():
    console_log("INFO", "console log info msg")

    console_log("WARN", "console log warn msg")

    console_log("ERRO", "console log erro msg")

    log_info("info msg")

    log_warn("warn msg")

    log_erro("erro msg")

################################################################################
if __name__ == "__main__":
    main()
