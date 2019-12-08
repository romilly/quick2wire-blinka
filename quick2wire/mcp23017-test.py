import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from digitalio import Direction
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

pin0 = mcp.get_pin(0)
pin0.direction = Direction.OUTPUT

while True:
    pin0.value = True
    sleep(1)
    pin0.value = False
    sleep(1)

