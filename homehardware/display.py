from atexit import register as atexit

from hd44780 import HD44780


display = HD44780()


@atexit
def cleanup_display():
    display.clear()
    display.backlight(False)


def display_text(text):
    display.clear()

    if not text:
        display.backlight(False)
        return

    text = text.splitlines()  # Separate lines
    text = [i[:20] for i in text]  # Cut at line end
    while len(text) < 4:
        text.append('')  # Add empty lines if too few

    for i in range(4):
        display.position(i, 0)
        display.write(text[i])
    display.backlight(True)
