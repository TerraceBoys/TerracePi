import usb.core
import usb.util
import sys

# find our device
dev = usb.core.find(idVendor=0x1d34, idProduct=0x000d)

# was it found?
if dev is None:
    raise ValueError('Device not found')
    
dev.set_configuration()


for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')