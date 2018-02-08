#!/usr/bin/env python3

import asyncio
import datetime


def display_date(loop):
    print('At the tone, the time will be {time} -- BEEP!'.format(
        time=datetime.datetime.now().strftime('%H:%M:%S')
    ))
    loop.call_later(10, display_date, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(display_date, loop)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
