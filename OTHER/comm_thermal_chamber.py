import minimalmodbus
import sys
from time import sleep

__author__ = "[bernard.cloutier@ge.com]"
__version__ = "1.0.0"


class ThermalChamber(object):

    def __init__(self, port, slave=1):
        self.instrument = minimalmodbus.Instrument(port, slave)
        self.instrument.serial.baudrate = 9600
        self.instrument.debug = False

    def get_temperature(self):
        sleep(1)
        return self.instrument.read_register(100, 1, signed=True)

    def set_temperature(self, temperature):
        sleep(1)
        self.instrument.write_register(300, temperature, 1, signed=True)

    @property
    def temp(self):
        return self.get_temperature()

    @temp.setter
    def temp(self, value):
        self.set_temperature(value)


def configure_thermal_chamber(COM_port):
    try:
        chamber = ThermalChamber(COM_port)
        return chamber
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    try:
        COM_port = sys.argv[1]
        chamber = configure_thermal_chamber(COM_port)
        if len(sys.argv) > 2:
            _set_new_temperature = float(sys.argv[2])
            print _set_new_temperature
            chamber.set_temperature(_set_new_temperature)
        else:
            print chamber.get_temperature()
    except Exception as e:
        print e
