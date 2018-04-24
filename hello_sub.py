#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import capnp
import hello_capnp

msg = hello_capnp.Message.new_message()
msg.value = "hello world"

#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5559")
socket.setsockopt(zmq.SUBSCRIBE, b'')

#  Do 10 requests, waiting each time for a response
for request in range(1,11):
    message = socket.recv()
    hellos = hello_capnp.Message.read_multiple_bytes(message)
    print("Received reply %s [%s]" % (request, hellos.next()))
