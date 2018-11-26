from tuning import Tuning
import usb.core
import usb.util
import time

print("test")
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
#print dev
if dev:
    Mic_tuning = Tuning(dev)
    print("enable")
    while True:
        try:
            if Mic_tuning.is_voice():
                print Mic_tuning.direction
                time.sleep(1)
        except KeyboardInterrupt:
            print "error"
            break
