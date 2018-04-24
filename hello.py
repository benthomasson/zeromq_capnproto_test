#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import capnp
import hello_capnp

msg = hello_capnp.Message.new_message()
msg.value = "hello world"

print (msg)
