import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

address = 0x48

def read(chn): #channel
	try:
		if chn == 0:
			bus.write_byte(address,0x40)
		if chn == 1:
			bus.write_byte(address,0x41)
		if chn == 2:
			bus.write_byte(address,0x42)
		if chn == 3:
			bus.write_byte(address,0x43)
		bus.read_byte(address) # dummy read to start conversion
	except Exception as e:
		print ("Address: %s" % address)
		print (e)
	return bus.read_byte(address)

while True:
    print(read(0))