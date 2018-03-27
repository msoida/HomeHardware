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
        printer.print_title(fill(unidecode(title.strip()), width=32))
    printer.set_align('middle')
    printer.write(fill(unidecode(text.strip()), width=30))
    printer.end_printing()
