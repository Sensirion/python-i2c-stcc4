Execute measurements with SensorBridge
=======================================

The following steps show how to use this driver on a Windows system using the `Sensirion SEK-SensorBridge`_ to
execute a simple measurement.

1. Install the STCC4 driver and all required packages as described in :ref:`Installation`.
2. Install the driver for the `Sensirion SEK-SensorBridge`_

   .. sourcecode:: bash

        pip install sensirion-shdlc-sensorbridge

3. Connect the SEK-SensorBridge to your PC over USB

   a. If the SEK-SensorBridge is not detected by your system, follow the  `SensorBridge FTDI Driver Installation`_

4. Connect the STCC4 sensor to the SEK-SensorBridge
5. Run the example script from the root of the repository.

   By default the script assumes the SensorBridge is connected to :code:`COM1` serial port. If this is different on your system,
   pass the port in use with the :code:`--serial-port` parameter as outlined below.

   .. sourcecode:: bash

        python examples/example_usage_sensorbridge_stcc4.py --serial-port <your COM port>


.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/product-support/sek-sensorbridge/
.. _SensorBridge FTDI Driver Installation: https://sensirion.github.io/python-shdlc-sensorbridge/sensor-bridge-installation.html

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../examples/example_usage_sensorbridge_stcc4.py
    :language: python

Execute measurements using internal Linux I²C driver
====================================================

On Linux systems it is furthermore possible to use the Linux user space I²C driver directly.
How this can be done is shown in the following.

1. Install the STCC4 driver and all required packages as described in :ref:`Installation`.
2. Connect the STCC4 sensor to the I²C port of your system (for example to the I²C port 1 of a Raspberry Pi).
3. Run the example script from the root of the repository.

   By default the script assumes you have the sensor connected to :code:`/dev/i2c-1`.
   If this is different on your system, pass the port in use with the :code:`--i2c-port` parameter as outlined below.

   .. sourcecode:: bash

      python examples/example_usage_linux_stcc4.py --i2c-port <your I2C port>

Example script
~~~~~~~~~~~~~~

.. literalinclude:: ../examples/example_usage_linux_stcc4.py
    :language: python
