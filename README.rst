==================
Barrenero Telegraf
==================

Extension for Barrenero that harvests information and send it using Telegraf.

:Version: 1.0.0
:Status: Production/Stable
:Author: José Antonio Perdiguero López

This extension provides an automatic way of harvesting Barrenero status through its API and send it through Telegraf.

Full `documentation <http://barrenero.readthedocs.io>`_ for Barrenero project.

Help us Donating
----------------

This project is free and open sourced, you can use it, spread the word, contribute to the codebase and help us donating:

:Ether: 0x566d41b925ed1d9f643748d652f4e66593cba9c9
:Bitcoin: 1Jtj2m65DN2UsUzxXhr355x38T6pPGhqiA
:PayPal: barrenerobot@gmail.com

Requirements
------------

* Python 3.5 or newer. Download `here <https://www.python.org/>`_.
* Docker. `Official docs <https://docs.docker.com/engine/installation/>`_.


Quick start
-----------
1. Install services:
    
    .. code:: console

        sudo ./make install <influxdb_url> <influxdb_database> <influxdb_username> <influxdb_password>

2. Move to installation folder:

    .. code:: console

        cd /usr/local/lib/barrenero/barrenero-telegraf/

3. Build the service:

    .. code:: console

        ./make build

4. Reboot or restart Systemd unit:

    .. code:: console

        sudo service barrenero_telegraf restart

Systemd
-------

The project provides a service file for Systemd that will be installed. These service files gives a reliable way to run
each miner, as well as overclocking scripts.

To check a miner service status:

.. code:: console

    service barrenero_telegraf status

Run manually
------------

As well as using systemd services you can run miners manually using:

.. code:: console

    ./make run
