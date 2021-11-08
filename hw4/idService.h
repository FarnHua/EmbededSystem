#ifndef __BLE_id_SERVICE_H__
#define __BLE_id_SERVICE_H__



class idService {
public:
    const static uint16_t id_SERVICE_UUID        = 0xB000;
    const static uint16_t id_CHARACTERISTIC_UUID = 0xB001;


    idService(BLE &_ble, char* idInitial) :
        ble(_ble), id(id_CHARACTERISTIC_UUID, idInitial, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY)
    {
        GattCharacteristic *charTable[] = {&id};
        GattService         idService(idService::id_SERVICE_UUID, charTable, sizeof(charTable) / sizeof(GattCharacteristic *));

        ble.gattServer().addService(idService);
    }

    void updateButtonState(char*  newState) {
        ble.gattServer().write(id.getValueHandle(), (uint8_t *)newState, 10);
    }

  

private:
    BLE                              &ble;
    ReadOnlyArrayGattCharacteristic<char,10>  id;
    
};
#endif /* #ifndef __BLE_id_SERVICE_H__ */
