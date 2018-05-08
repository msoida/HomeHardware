from textwrap import fill

from serial import serial_for_url
from unidecode import unidecode

from thermal import ThermalPrinter

from .settings import printer_url


printer = ThermalPrinter('-', printer=serial_for_url(printer_url))
printer.reset()
printer.set_parameters(max_heating_dots=250, heating_time=250)


def print_message(text, title=None):
    if title is not None:
        title = unidecode(title.strip())
        title = '\n'.join([fill(i, width=28) for i in title.splitlines()])
        printer.print_title(title)
    text = unidecode(text.strip())
    text = '\n'.join([fill(i, width=30) for i in text.splitlines()])
    printer.set_align('middle')
    printer.write(text)
    printer.end_printing()
