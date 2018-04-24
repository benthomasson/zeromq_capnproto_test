#!/usr/bin/env python
# -*- coding: utf-8 -*-

import coverage
import a_lib


cov = coverage.Coverage()
cov.set_option("run:branch", True)
cov.start()

a_lib.woo()

cov.stop()

data = cov.get_data()
print(data.run_infos())
for f in data.measured_files():
    print (f, data.lines(f))
    print (f, data.arcs(f))
