#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import capnp
import measurements_capnp
import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5559")
socket.setsockopt(zmq.SUBSCRIBE, b'')

#  Do 10 requests, waiting each time for a response
for request in range(1,11):
    message = socket.recv_multipart()
    if message[0] == "Measurements":
        samples = measurements_capnp.Measurements.read_multiple_bytes(message[1])
        print("Received reply %s [%s]" % (request, samples.next()))
