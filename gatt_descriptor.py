#Service [6e400001-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]    Characteristic [6e400002-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]    Characteristic [6e400003-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]  Service [00001801-0000-1000-8000-00805f9b34fb]

import gatt

from argparse import ArgumentParser


class AnyDevice(gatt.Device):
    def connect_succeeded(self):
        super().connect_succeeded()
        print("[%s] Connected" % (self.mac_address))

    def connect_failed(self, error):
        super().connect_failed(error)
        print("[%s] Connection failed: %s" % (self.mac_address, str(error)))

    def disconnect_succeeded(self):
        super().disconnect_succeeded()
        print("[%s] Disconnected" % (self.mac_address))

    def services_resolved(self):
        super().services_resolved()

        print("[%s] Resolved services" % (self.mac_address))
        for service in self.services:
            print("[%s]\tService [%s]" % (self.mac_address, service.uuid))
            for characteristic in service.characteristics:
                print("[%s]\t\tCharacteristic [%s]" % (self.mac_address, characteristic.uuid))
                for descriptor in characteristic.descriptors:
                    print("[%s]\t\t\tDescriptor [%s] (%s)" % (self.mac_address, descriptor.uuid, descriptor.read_value()))

    def descriptor_read_value_failed(self, descriptor, error):
        print('descriptor_value_failed')


arg_parser = ArgumentParser(description="GATT Connect Demo")
arg_parser.add_argument('mac_address', help="MAC address of device to connect")
args = arg_parser.parse_args()

print("Connecting...")

manager = gatt.DeviceManager(adapter_name='hci0')

device = AnyDevice(manager=manager, mac_address=args.mac_address)
device.connect()

manager.run()
