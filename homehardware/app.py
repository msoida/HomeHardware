from .clock import clock_tick, update_text
from .connection import client
# from .display import display_text
from .leds import leds_tick, update_leds
from .printer import print_message


client.user_data_set(dict(
    clock_text=update_text,
    # display_text=display_text,
    printer_text=print_message,
    leds_value=update_leds,
))


def main_loop():
    clock_tick()
    leds_tick()
