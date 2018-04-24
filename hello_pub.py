#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import capnp
import hello_capnp

msg = hello_capnp.Message.new_message()
msg.value = "hello world"

print (msg)
#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5559")

while True:
    socket.send(msg.to_bytes())
    msg.clear_write_flag()
    print ('.')
