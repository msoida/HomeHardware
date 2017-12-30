from atexit import register as atexit
from datetime import datetime, timedelta

from pytz import utc

from sn3218 import SN3218


leds = SN3218()
leds.reset()
leds.output(True)
leds.channel_mask([1] * 18)


@atexit
def run_at_exit():
    leds.output(False)


def leds_tick():
    lastupdate = leds_tick.__dict__.get('lastupdate',
                                        (datetime(1970, 1, 1, tzinfo=utc)))
    now = datetime.now(utc)

    # p = [0] * 12
    # powr = 0

    output = [0] * 18
    # output = [0, p[0], p[1], powr, p[2], p[3], 0, p[4], p[5], powr,
    #           p[6], p[7], 0, p[8], p[9], powr, p[10], p[11]]

    if (now - lastupdate > timedelta(seconds=5)):
        lastupdate = now
        for i, val in enumerate(output, start=1):
            # print('{}: {}'.format(i,val))
            leds.channel(i, val)


def update_leds():
    pass
