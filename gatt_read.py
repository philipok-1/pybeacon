#Service [6e400001-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]    Characteristic [6e400002-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]    Characteristic [6e400003-b5a3-f393-e0a9-e50e24dcca9e]
#[D1:0E:28:2D:71:AA]  Service [00001801-0000-1000-8000-00805f9b34fb]

import gatt

manager = gatt.DeviceManager(adapter_name='hci0')

class AnyDevice(gatt.Device):
    def services_resolved(self):
        super().services_resolved()

        device_information_service = next(
            s for s in self.services
            if s.uuid == '6e400001-b5a3-f393-e0a9-e50e24dcca9e')

        firmware_version_characteristic = next(
            c for c in device_information_service.characteristics
            
            if c.uuid == '6e400002-b5a3-f393-e0a9-e50e24dcca9e')


        firmware_version_characteristic.write_value("E.getTemperature()\n".encode("UTF-8"))
        firmware_version_characteristic.enable_notifications()
        firmware_version_characteristic.read_value()


    def characteristic_value_updated(self, characteristic, value):
        print("Firmware version:", value.decode("utf-8"))


device = AnyDevice(mac_address='d1:0e:28:2d:71:aa', manager=manager)
device.connect()

manager.run()
