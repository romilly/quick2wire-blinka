import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

address = 0x48

bus = busio.I2C(board.SCL, board.SDA)

_BUFFER = bytearray(3)

class PCF8591():
    def _read_u8(self, register):
        # Read an unsigned 8 bit value from the specified 8-bit register.
        with self._device as i2c:
            _BUFFER[0] = register & 0xFF

            i2c.write_then_readinto(_BUFFER, _BUFFER, out_end=1, in_start=1, in_end=2)
            return _BUFFER[1]

    def read(self):
        return self._read_u8(0x40)

chip = PCF8591()

while True:
    print(chip.read())