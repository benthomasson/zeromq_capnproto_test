#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    emit_event [options] <name>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from __future__ import print_function
from docopt import docopt
import logging
import sys
import capnp # noqa
import measurements_capnp
import psutil
import zmq
import time
import datetime
from itertools import count

logger = logging.getLogger('emit_event')


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect("tcp://127.0.0.1:5560")

    counter = count(0)
    event(socket, counter, parsed_args['<name>'])

    return 0


def event(socket, counter, name):
    timestamp = datetime.datetime.utcnow().isoformat()
    event = measurements_capnp.Event.new_message()
    event.timestamp = timestamp
    event.id = next(counter)
    event.name = name
    socket.send_multipart([b"Event", event.to_bytes()])


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))
