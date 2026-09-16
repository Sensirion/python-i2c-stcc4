# Python I2C Driver for Sensirion STCC4

This repository contains the Python driver to communicate with a Sensirion STCC4 sensor over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-stcc4/master/images/STCC4.png"
    width="300px" alt="STCC4 picture">


Click [here](https://sensirion.com/products/catalog/STCC4) to learn more about the Sensirion STCC4 sensor.


The STCC4 is Sensirion's next generation miniature CO2 sensor for indoor air quality applications.



The default I²C address of [STCC4](https://sensirion.com/products/catalog/STCC4) is **0x64**.

> [!NOTE]
> The SEK-STCC4 board from Sensirion includes a STCC4 and a SHT4x for temperature and humidity compensation, which is controlled by the STCC4 through the integrated I2C controller interface. The provided examples are designed considering this sensor configuration.

## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-stcc4/master/images/STCC4_pinout.png"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | black | GND | Ground |
| 2 | red | VDD | Supply Voltage | 2.7V to 5.5V
| 3 | green | SDA | I2C: Serial data input / output |
| 4 | yellow | SCL | I2C: Serial clock input |


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-stcc4) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-stcc4/quickstart.html) example.


## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-stcc4/contributing.html)).

## License

See [LICENSE](LICENSE).