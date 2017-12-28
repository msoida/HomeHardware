from .clock import clock_tick, update_text
from .connection import client

client.userdata = dict(clock_text=update_text)

def main_loop():
    clock_tick()
