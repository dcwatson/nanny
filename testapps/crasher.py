#!/usr/bin/env python3

import asyncio
import random
import sys


def maybe_crash(loop):
    if random.random() < 0.2:
        print('crashing')
        sys.exit(1)
    print('still alive!')
    loop.call_later(5, maybe_crash, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(maybe_crash, loop)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
