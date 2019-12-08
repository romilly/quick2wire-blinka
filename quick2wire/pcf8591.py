import board
import busio
from time import sleep
from adafruit_bus_device import i2c_device

i2c = busio.I2C(board.SCL, board.SDA)


_BUFFER = bytearray(3)

class PCF8591():
    def __init__(self, i2c, address=0x48):
        self._device = i2c_device.I2CDevice(i2c, address)

    def _read_u8(self, register):
        # Read an unsigned 8 bit value from the specified 8-bit register.
        with self._device as i2c:
            _BUFFER[0] = register & 0xFF

            i2c.write_then_readinto(_BUFFER, _BUFFER, out_end=1, in_start=1, in_end=2)
            return _BUFFER[1]

    def read(self):
        return self._read_u8(0x40)

chip = PCF8591(i2c)

while True:
    print(chip.read())
    sleep(1)
