#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import coverage
cov = coverage.Coverage()
cov.start()

import capnp # noqa
import measurements_capnp
import psutil
import zmq
import time
import datetime
from itertools import count
import a_lib

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5559")

counter = count(0)

while True:
    timestamp = datetime.datetime.utcnow().isoformat()
    cov.stop
    data = cov.get_data()
    sample = measurements_capnp.Measurements.new_message()
    sample.timestamp = timestamp
    sample.id = next(counter)
    sample.cpu.cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    sample.memory.total = mem.total
    sample.memory.available = mem.available
    sample.memory.percent = mem.percent
    sample.memory.used = mem.used
    sample.memory.free = mem.free
    sample.memory.active = mem.active
    sample.memory.inactive = mem.inactive
    sample.memory.wired = mem.wired
    files = data.measured_files()
    for cf, sf in zip(files, sample.coverage.init('files', len(files))):
        sf.path = cf
        lines = data.lines(cf)
        for cl, sl in zip(lines, sf.init('lines', len(lines))):
            sl.lineno = cl
    socket.send(sample.to_bytes())
    cov = coverage.Coverage()
    cov.start()
    a_lib.woo()
    time.sleep(1)
