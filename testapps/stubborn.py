#!/usr/bin/env python3

import asyncio
import signal
import os


def term_handler():
    print('Got SIGTERM, ignoring')


def int_handler():
    print('Got SIGINT, ignoring')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    if os.name == 'posix':
        loop.add_signal_handler(signal.SIGTERM, term_handler)
        loop.add_signal_handler(signal.SIGINT, int_handler)
    loop.run_forever()
