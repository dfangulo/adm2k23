import wmi

def numero_de_serie_bios():
    c = wmi.WMI()

    for item in c.Win32_ComputerSystemProduct():
        serial_number = item.IdentifyingNumber
    return serial_number

def numero_de_serie_baseboard():
    c = wmi.WMI()
    for item in c.Win32_BaseBoard():
        serial_number = item.SerialNumber
    return serial_number