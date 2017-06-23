from model.configurations import temperature_id


def get_actual_temperature():
    # 1-wire Slave Datei lesen
    try:
        file = open('/sys/bus/w1/devices/' + temperature_id + '/w1_slave')
    except IOError:
        print("There is no temperature sensor with the id: " + temperature_id)
        return "No temperature"
    file_content = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    string_value = file_content.split("\n")[1].split(" ")[9]
    temperature = float(string_value[2:]) / 1000

    # Temperatur ausgeben
    return_value = '%6.2f' % temperature
    return str(return_value)
