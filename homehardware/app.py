from .clock import clock_tick, update_text
from .connection import client
from .display import display_text


client.user_data_set(dict(
    clock_text=update_text,
    display_text=display_text,
))


def main_loop():
    clock_tick()
