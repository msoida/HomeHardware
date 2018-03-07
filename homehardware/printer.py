from serial import serial_for_url

from thermal import ThermalPrinter

from .settings import printer_url


printer = ThermalPrinter('-', printer=serial_for_url(printer_url))
printer.reset()
printer.set_parameters(max_heating_dots=250, heating_time=250)


def print_message(text, title=None):
    if title is not None:
        printer.print_title(title.strip())
    printer.set_align('middle')
    printer.write(text.strip())
    printer.end_printing()
