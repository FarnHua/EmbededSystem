#ifndef __BLE_led_SERVICE_H__
#define __BLE_led_SERVICE_H__



class ledService {
public:
    const static uint16_t led_SERVICE_UUID        = 0xC000;
    const static uint16_t led_CHARACTERISTIC_UUID = 0xC001;


    ledService(BLE &_ble, bool ledinitial) :
        ble(_ble), led(led_CHARACTERISTIC_UUID, &ledinitial, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY)
    {
        GattCharacteristic *charTable[] = {&led};
        GattService         ledService(ledService::led_SERVICE_UUID, charTable, sizeof(charTable) / sizeof(GattCharacteristic *));

        ble.gattServer().addService(ledService);
    }

    

  

private:
    BLE                              &ble;
    ReadWriteGattCharacteristic<bool> led;
};
#endif /* #ifndef __BLE_led_SERVICE_H__ */
