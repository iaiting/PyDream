#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import keyring
def register(username, password):
    keyring.set_password("xsmtp", username, password)