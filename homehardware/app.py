import atexit
from datetime import datetime, timedelta

from pytz import utc, timezone

from ht16k337segment import HT16K337Segment

from .connection import client


tz = timezone('Europe/Warsaw')
lastupdate = datetime(1970, 1, 1, tzinfo=utc)
clock = HT16K337Segment()


@atexit.register
def run_at_exit():
    clock.display(False)


def clock_tick():
    lastupdate = clock_tick.__dict__.get('lastupdate',
                                         (datetime(1970, 1, 1, tzinfo=utc)))
    now = datetime.now(utc)

    numbers = list(now.astimezone(tz).strftime('%H%M'))
    sec = (now.second % 2) == 0

    if (now.hour > 6) and (now.hour < 20):
        brightness = 5
    else:
        brightness = 0

    clock.colon(sec)
    if (now - lastupdate > timedelta(seconds=5)):
        lastupdate = now
        clock.brightness(brightness)
        for i in range(4):
            clock.write_digit(i, numbers[i])


def main_loop():
    clock_tick()
