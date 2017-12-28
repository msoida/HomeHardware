import atexit
from datetime import datetime, timedelta

from pytz import utc, timezone

from ht16k337segment import HT16K337Segment


tz = timezone('Europe/Warsaw')
clock = HT16K337Segment()
clocknumbers = None
clockcolon = False
clockbrightness = 0


@atexit.register
def run_at_exit():
    clock.display(False)


def clock_tick():
    lastupdate = clock_tick.__dict__.get('lastupdate',
                                         (datetime(1970, 1, 1, tzinfo=utc)))
    now = datetime.now(utc)

    if clocknumbers:
        numbers = clocknumbers
        colon = clockcolon
        brightness = clockbrightness
    else:
        numbers = list(now.astimezone(tz).strftime('%H%M'))
        colon = (now.second % 2) == 0

        if (now.hour > 6) and (now.hour < 20):
            brightness = 5
        else:
            brightness = 0

    clock.colon(colon)
    if (now - lastupdate > timedelta(seconds=2)):
        lastupdate = now
        clock.brightness(brightness)
        for i in range(4):
            clock.write_digit(i, numbers[i])


def update_text(text, brightness=5):
    global clocknumbers, clockcolon, clockbrightness
    if not text:
        clocknumbers = None
        return
    text = str(text) + '    '
    if text[2] == ':':
        clocknumbers = [text[0], text[1], text[3], text[4]]
        clockcolon = True
    else:
        clocknumbers = list(text[:4])
        clockcolon = False
    clockbrightness = brightness
